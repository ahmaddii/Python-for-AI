import requests

webhook_url = "https://webhook.site/your-test-url"

data = {
            "event": "quotesScraped",
            "count": 10
}

# webhook sends data automatically when something like form api call or other thing happend

response = requests.post(webhook_url,json=data)

print(response.status_code)