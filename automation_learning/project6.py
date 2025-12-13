import requests

url = "https://webhook.site/650ae358-2f3c-4bb4-8d45-8384d678e940"

data = {

            "event": "web-scraped",
            "count": 10
}

response = requests.post(url,json=data)

print(f"Data has beed sent with Status Code {response.status_code}") # tell data sent or not 