import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print(data)

# for extraction

for user in data:
            print("Name: ",user["name"])
            print("Email: ", user["email"])
            print("-" * 30)