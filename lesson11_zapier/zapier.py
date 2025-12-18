import requests
from datetime import datetime
import google.generativeai as genai
import json


API_URL = ""
WEBHOOK_URL = ""


genai.configure(api_key=API_URL)
model = genai.GenerativeModel("gemini-2.5-flash")

text = "Javascript is good"


prompt = f"""

Classify the following text as one of:
Motivational, Technical, Philosophical or raw one
Respond with ONE word only.

Text:

{text}

"""

ai_response = model.generate_content(prompt)

category = ai_response.text.strip()


payload = {

            "text": text,
            "category": category,
            "timestamp": datetime.now().isoformat(),
            "source": "lesson11_zapier"

}

response = requests.post(WEBHOOK_URL,json=payload)

print("AI Category ",category)
print("Data Successfully Sent with Code ",response.status_code)


