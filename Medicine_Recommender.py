{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO5yWoktTd/MApI/wUwJcAO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Imran25git/Practice-projects/blob/My-Codes/Medicine_Recommender.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Note: Please make sure that you have to consult a doctor before using any recommended medicine....\")\n",
        "print(\"Using below recommended medicine is on your own risk so please consult doctor if disease is going prolong by time\")\n",
        "print(\"\\n\")\n",
        "\n",
        "print(\"This app will not respond or recommend medicine if your input situation or disease is critical\")\n",
        "print(\"This app will only recommend medicine if your input disease is mild or not in harsh situation. The mild disease are as follow:-\")\n",
        "print(\"\\n\")\n",
        "mild = \"\"\"\\b\\bfever\n",
        "cold\n",
        "flu\n",
        "headache\n",
        "cough\n",
        "stomach pain\n",
        "acidity\n",
        "dhirea\n",
        "vomiting\n",
        "body pain\"\"\"\n",
        "print(mild)\n",
        "print(\"\\n\")\n",
        "situation = input(\"Enter your disease situation (critical or mild): \").lower()\n",
        "if situation == \"critical\":\n",
        "  print(\"YOU HAVE CRITICAL CONDITION. FOR THIS CONSULT A DOCTOR QUICKLY!!!\")\n",
        "  exit()\n",
        "elif situation == \"mild\":\n",
        "  print(\"READ INSTRUCTIONS FROM ABOVE BEFORE USING ANY MEDICINE GIVEN BELOW\\n\")\n",
        "  disease = input(\"Enter your disease or name of illness here: \").lower()\n",
        "  if disease == \"fever\":\n",
        "    print(\"The medicine recommended for having fever is: paracetamol or ibrufen\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"cold\":\n",
        "    print(\"The medicine recommended for having cold is: Antihistamines\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"flu\":\n",
        "    print(\"The medicine recommended for having flu is: ibrufen\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"headache\":\n",
        "    print(\"The medicine recommended for having Headache is: paracetamol\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease ==  \"cough\":\n",
        "    print(\"The medicine recommended for having cough is: Acyfyl\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"stomach pain\":\n",
        "    print(\"The medicine recommended for having stomach pain is: Omeprazole for gas flygel is best\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"acidity\":\n",
        "    print(\"The medicine recommended for having acidity is: Risek\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"dhirea\":\n",
        "    print(\"The medicine recommended for having dhirea is: ORS Sachet\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"vomiting\":\n",
        "    print(\"The medicine recommended for having vomiting is: Domperidone\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  elif disease == \"body pain\":\n",
        "    print(\"The medicine recommended for having body pain is: paracetamol\")\n",
        "    print(\"\\a\\a\\a\\aRECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \")\n",
        "  else:\n",
        "    print(f\"YOU MUST HAVE TO CONSULT A DOCTOR FOR YOUR {disease} DISEASE...\\a\\a\\a\\a\")\n",
        "else:\n",
        "  print(\"You had input something wrong\")\n",
        "  exit()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FkP4yWawrUyi",
        "outputId": "db527ed6-5ffe-46e8-aa99-9ab020d74657"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Note: Please make sure that you have to consult a doctor before using any recommended medicine....\n",
            "Using below recommended medicine is on your own risk so please consult doctor if disease is going prolong by time\n",
            "\n",
            "\n",
            "This app will not respond or recommend medicine if your input situation or disease is critical\n",
            "This app will only recommend medicine if your input disease is mild or not in harsh situation. The mild disease are as follow:-\n",
            "\n",
            "\n",
            "\b\bfever\n",
            "cold\n",
            "flu\n",
            "headache\n",
            "cough\n",
            "stomach pain\n",
            "acidity\n",
            "dhirea\n",
            "vomiting\n",
            "body pain\n",
            "\n",
            "\n",
            "Enter your disease situation (critical or mild): mild\n",
            "READ INSTRUCTIONS FROM ABOVE BEFORE USING ANY MEDICINE GIVEN BELOW\n",
            "\n",
            "Enter your disease or name of illness here: fever\n",
            "The medicine recommended for having fever is: paracetamol or ibrufen\n",
            "\u0007\u0007\u0007\u0007RECOMMENDED: CONSULT A DOCTOR IS GOOD FOR SAFE SIDE!!! \n"
          ]
        }
      ]
    }
  ]
}