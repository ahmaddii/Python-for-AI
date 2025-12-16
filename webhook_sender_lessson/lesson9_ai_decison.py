import requests
from datetime import datetime
import google.generativeai as genai

WEBHOOK_URL =  "https://webhook.site/650ae358-2f3c-4bb4-8d45-8384d678e940"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


text_to_classfiy = """
Debugging is twice as hard as writing the code in the first place.
"""

prompt = f"""

Classify the following text as one of these categories:
- Motivational
- Philosophical
- Technical

Respond with ONLY one word.

Text:

{text_to_classfiy}


"""

model_response = model.generate_content(prompt)

category = model_response.text.strip()


if category == "Technical":
            action = "send_to_dev_sheet"

elif category == "Philosophical":
        action = "send to philosy"

elif category == "Motivational":
        action = "send_to_quotes"

else:
        action = "Manual-review"

payload = {

            "event": "text sending",
            "text": text_to_classfiy.strip(),
            "time": datetime.now().isoformat(),
            "category": category,
            "action": action
}

response = requests.post(WEBHOOK_URL,json=payload)

print("AI Categroy", category)
print("Action Chosen ",action)
print("Webhook reponse ", response.status_code)

