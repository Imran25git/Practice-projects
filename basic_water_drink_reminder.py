# Basic Water drinking reminder code

# If we perform in colab we use ! before pi but in offline editor we use just pip to install module
!pip install pytz

from datetime import datetime
import time
import pytz

karachi_tz = pytz.timezone('Asia/Karachi')

# Get the current time in Karachi
current_time = datetime.now(karachi_tz).strftime("%I:%M %p")

print(f"Current time in Karachi: {current_time}")
set_time = int(input("Enter time to get reminder for drinking water in minutes: "))
print(f"Ok you will get reminder after {set_time} minutes")
time.sleep(set_time*60)
print("\a"*5)
print("Reminder!!!! Drink Water")
