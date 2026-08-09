"""
ScamShield - Hybrid AI Scam Message Detector (Single File Version)
Iris Hacks IV - Team Money Heist

Run with: python scamshield_app.py
Then open: http://127.0.0.1:5000

BEFORE RUNNING:
1. pip install flask openai
2. Set your Featherless API key as an environment variable:
   Mac/Linux:  export FEATHERLESS_API_KEY="your_key_here"
   Windows:    set FEATHERLESS_API_KEY=your_key_here
3. Confirm MODEL_NAME below matches a model available on your Featherless account.
"""

import os
import sys
import json
from flask import Flask, render_template_string, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# ---------------------------------------------------------------
# CONFIG - check these first if something breaks
# ---------------------------------------------------------------
FEATHERLESS_API_KEY = os.environ.get("FEATHERLESS_API_KEY", "")
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"  # confirm this matches your Featherless workshop model

if not FEATHERLESS_API_KEY:
    print("=" * 70)
    print("WARNING: FEATHERLESS_API_KEY environment variable is not set.")
    print("The app will run, but every analysis request will fail until")
    print("you set it. Example:")
    print('  export FEATHERLESS_API_KEY="your_key_here"')
    print("=" * 70)

client = OpenAI(
    base_url="https://api.featherless.ai/v1",
    api_key=FEATHERLESS_API_KEY or "MISSING_KEY",
)

# ---------------------------------------------------------------
# LAYER 1: Fast local keyword pre-check (evolved from our original
# basic spam filter - never blocks by itself, just hints to the AI
# and gives an instant visual flag in the UI)
# ---------------------------------------------------------------
LOCAL_RED_FLAG_PHRASES = [
    "verify now", "account will be blocked", "click this link", "claim your prize",
    "you have won", "customs fee", "clearance fee", "send your cnic",
    "bank details", "sim will be blocked", "act now", "limited time",
    "urgent action required", "confirm your account",
]

LOCAL_SCAM_EXAMPLES = [
    "Your JazzCash account will be blocked in 24 hours. Verify now: bit.ly/xyz",
    "Congratulations! You have won PKR 500,000 in the Easypaisa lucky draw. Share your account details to claim.",
    "Your parcel is held at customs. Pay a 500 PKR clearance fee to release it: [link]",
    "We are hiring for online data entry job, PKR 80,000/month, no experience needed. Send CNIC and bank details to start.",
    "Dear customer your SIM will be blocked today, call this number immediately to avoid suspension.",
]


def local_pre_check(text: str) -> dict:
    text_lower = text.lower()
    matched = [p for p in LOCAL_RED_FLAG_PHRASES if p in text_lower]
    return {"quick_flag": len(matched) > 0, "matched_phrases": matched}


SYSTEM_PROMPT = f"""You are ScamShield, an assistant that helps everyday people -
especially parents, grandparents, and people who are not tech-savvy -
understand whether a message they received might be a scam.

You must respond ONLY in valid JSON, with no extra text before or after, using this exact shape:
{{
  "verdict": "Likely Scam" | "Possibly Suspicious" | "Likely Safe",
  "confidence": a number from 0 to 100,
  "why": "A short, simple explanation in plain everyday language. No jargon like 'phishing'. Explain the manipulation tactic in human terms, e.g. 'This message is trying to make you panic so you act before thinking.'",
  "tactic": "One short label, e.g. Urgency, Fear, Fake Authority, Too-Good-To-Be-True, Impersonation, or None",
  "advice": "One or two clear, simple sentences on what the person should do next.",
  "safe_reply": "A short, polite message the person could send back if replying is reasonably safe, OR the string 'Do not reply - block and report' if replying at all is risky."
}}

Here are real local scam message patterns to help you recognize similar ones (Pakistan context - JazzCash, Easypaisa, courier/customs scams, fake job offers, fake SIM block messages):
{chr(10).join(f"- {ex}" for ex in LOCAL_SCAM_EXAMPLES)}

Be practical, calm, and kind - like explaining this to a family member.
Do not be alarmist about genuinely safe, everyday messages.
Base your verdict on the full context and intent of the message, not just individual words.
No detector is ever 100% certain - reflect genuine uncertainty in your confidence score when appropriate.
"""


def ai_analyze(message: str, pre_check: dict) -> dict:
    hint = ""
    if pre_check["quick_flag"]:
        hint = (
            f"\n\n(Note: our local scanner flagged these common scam phrases: "
            f"{', '.join(pre_check['matched_phrases'])}. Use as a hint only - "
            f"still judge the full context, as these phrases can appear in innocent messages too.)"
        )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Analyze this message:\n\n{message}{hint}"},
        ],
        temperature=0.3,
        max_tokens=400,
    )

    raw_text = response.choices[0].message.content.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        if raw_text.startswith("json"):
            raw_text = raw_text[4:].strip()

    return json.loads(raw_text)  # let this raise if malformed - caught by caller


# ---------------------------------------------------------------
# ROUTES
# ---------------------------------------------------------------

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/analyze", methods=["POST"])
def analyze():
    if not FEATHERLESS_API_KEY:
        return jsonify({
            "error": "FEATHERLESS_API_KEY is not set on the server. "
                     "Set it as an environment variable and restart the app."
        }), 500

    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Please paste a message to analyze."}), 400

    pre_check = local_pre_check(message)

    try:
        result = ai_analyze(message, pre_check)
        result["quick_flag"] = pre_check["quick_flag"]
        result["matched_phrases"] = pre_check["matched_phrases"]
        return jsonify(result)
    except json.JSONDecodeError:
        return jsonify({
            "error": "The AI's response wasn't valid JSON. Try again, or lower "
                     "temperature / adjust the prompt if this keeps happening."
        }), 500
    except Exception as e:
        # Print full detail to terminal for debugging, short message to browser.
        print("ERROR calling Featherless AI:", repr(e), file=sys.stderr)
        return jsonify({
            "error": f"AI request failed: {str(e)}. Check your API key, model "
                     f"name ('{MODEL_NAME}'), and internet connection."
        }), 500


# ---------------------------------------------------------------
# HTML/CSS/JS - all in one string, no templates folder needed
# ---------------------------------------------------------------
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>ScamShield - Is This Message a Scam?</title>
<style>
  :root {
    --safe: #2e7d32; --suspicious: #f9a825; --scam: #c62828;
    --bg: #f2f4fb; --card: #ffffff; --text: #1f2333; --muted: #6b7280; --accent: #3949ab;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); display: flex; justify-content: center; padding: 40px 16px; }
  .container { width: 100%; max-width: 660px; }
  header { text-align: center; margin-bottom: 28px; }
  header .logo { font-size: 2.4rem; }
  header h1 { margin: 6px 0 4px; font-size: 1.9rem; }
  header p { margin: 0; color: var(--muted); }
  .card { background: var(--card); border-radius: 16px; padding: 24px; box-shadow: 0 4px 16px rgba(31,35,51,0.06); margin-bottom: 20px; }
  textarea { width: 100%; min-height: 130px; padding: 14px; border-radius: 10px; border: 1px solid #e0e2ec; font-size: 1rem; font-family: inherit; resize: vertical; }
  textarea:focus { outline: 2px solid var(--accent); }
  button.primary { margin-top: 14px; width: 100%; padding: 14px; border: none; border-radius: 10px; background: var(--accent); color: white; font-size: 1rem; font-weight: 600; cursor: pointer; }
  button.primary:disabled { opacity: 0.6; cursor: not-allowed; }
  .examples { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
  .examples button { border: none; width: auto; margin-top: 0; background: #eef0fb; color: var(--accent); font-weight: 500; font-size: 0.82rem; padding: 8px 12px; border-radius: 8px; cursor: pointer; }
  #result { display: none; }
  .verdict-row { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }
  .verdict-badge { display: inline-block; padding: 6px 14px; border-radius: 20px; font-weight: 700; color: white; }
  .verdict-scam { background: var(--scam); }
  .verdict-suspicious { background: var(--suspicious); }
  .verdict-safe { background: var(--safe); }
  .confidence { color: var(--muted); font-size: 0.85rem; }
  .quick-flag { font-size: 0.78rem; background: #fff3e0; color: #e65100; padding: 4px 10px; border-radius: 8px; margin-bottom: 14px; display: inline-block; }
  .field { margin-bottom: 14px; }
  .field-label { font-weight: 600; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.03em; color: var(--muted); margin-bottom: 4px; }
  .field-value { font-size: 1rem; line-height: 1.5; }
  .loading { text-align: center; color: var(--muted); display: none; padding: 20px; }
  .error { color: var(--scam); text-align: center; display: none; padding: 10px; white-space: pre-wrap; }
  footer { text-align: center; color: var(--muted); font-size: 0.8rem; margin-top: 8px; }
</style>
</head>
<body>
<div class="container">
  <header>
    <div class="logo">&#128737;&#65039;</div>
    <h1>ScamShield</h1>
    <p>Paste a message. Get a simple, honest explanation - built to protect your family.</p>
  </header>

  <div class="card">
    <textarea id="messageInput" placeholder="Paste the SMS, WhatsApp message, or what a caller said..."></textarea>
    <div class="examples">
      <button onclick="useExample('Your JazzCash account will be blocked in 24 hours. Verify now: bit.ly/xyz')">Fake bank alert</button>
      <button onclick="useExample('Congratulations! You have won PKR 500,000. Share your account details to claim.')">Fake prize</button>
      <button onclick="useExample('We are hiring for online data entry job, PKR 80,000/month. Send CNIC and bank details to start.')">Fake job offer</button>
      <button onclick="useExample('Hi, are we still meeting for lunch tomorrow at 1pm?')">Safe message</button>
    </div>
    <button class="primary" id="analyzeBtn" onclick="analyzeMessage()">Analyze Message</button>
  </div>

  <div class="loading" id="loading">Analyzing message...</div>
  <div class="error" id="error"></div>

  <div class="card" id="result">
    <div class="verdict-row">
      <span id="verdictBadge" class="verdict-badge"></span>
      <span class="confidence" id="confidenceText"></span>
    </div>
    <div id="quickFlagBox"></div>
    <div class="field"><div class="field-label">Why</div><div class="field-value" id="whyText"></div></div>
    <div class="field"><div class="field-label">Tactic Used</div><div class="field-value" id="tacticText"></div></div>
    <div class="field"><div class="field-label">What To Do</div><div class="field-value" id="adviceText"></div></div>
    <div class="field"><div class="field-label">Suggested Reply</div><div class="field-value" id="replyText"></div></div>
  </div>

  <footer>ScamShield - Built by Team Money Heist for Iris Hacks IV</footer>
</div>

<script>
function useExample(text) { document.getElementById('messageInput').value = text; }

async function analyzeMessage() {
  const message = document.getElementById('messageInput').value.trim();
  const btn = document.getElementById('analyzeBtn');
  const loading = document.getElementById('loading');
  const errorBox = document.getElementById('error');
  const result = document.getElementById('result');

  errorBox.style.display = 'none';
  result.style.display = 'none';

  if (!message) {
    errorBox.textContent = 'Please paste a message first.';
    errorBox.style.display = 'block';
    return;
  }

  btn.disabled = true;
  loading.style.display = 'block';

  try {
    const res = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    let data;
    try {
      data = await res.json();
    } catch (parseErr) {
      throw new Error('Server did not return valid JSON (status ' + res.status + '). Check the terminal running python for the real error.');
    }

    if (!res.ok) {
      throw new Error(data.error || ('Request failed with status ' + res.status));
    }

    renderResult(data);
  } catch (err) {
    errorBox.textContent = err.message;
    errorBox.style.display = 'block';
  } finally {
    btn.disabled = false;
    loading.style.display = 'none';
  }
}

function renderResult(data) {
  const badge = document.getElementById('verdictBadge');
  badge.textContent = data.verdict;
  badge.className = 'verdict-badge ' +
    (data.verdict === 'Likely Scam' ? 'verdict-scam' :
     data.verdict === 'Possibly Suspicious' ? 'verdict-suspicious' : 'verdict-safe');

  document.getElementById('confidenceText').textContent =
    (data.confidence !== undefined) ? ('Confidence: ' + data.confidence + '%') : '';

  const quickFlagBox = document.getElementById('quickFlagBox');
  if (data.quick_flag && data.matched_phrases && data.matched_phrases.length) {
    quickFlagBox.innerHTML = '<span class="quick-flag">Quick scan flagged: ' + data.matched_phrases.join(', ') + '</span>';
  } else {
    quickFlagBox.innerHTML = '';
  }

  document.getElementById('whyText').textContent = data.why;
  document.getElementById('tacticText').textContent = data.tactic;
  document.getElementById('adviceText').textContent = data.advice;
  document.getElementById('replyText').textContent = data.safe_reply;

  document.getElementById('result').style.display = 'block';
}
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)