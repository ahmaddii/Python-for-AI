import requests
import json
from datetime import datetime

WEBHOOK_URL = "https://webhook.site/650ae358-2f3c-4bb4-8d45-8384d678e940"


data = {

            "event": "lesson 9",
            "source": "automation pipline",
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "payload": {
                        "message": "Python Successfully triggred and send data to webhook",
                        "level": "Beginner Automation"
            }

}

response = requests.post(WEBHOOK_URL,json=data)


print("Status Code",response.status_code)
print("Response ",response.text)