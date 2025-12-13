import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

with open("api_users.json","w") as file:

            json.dump(data,file,indent=4)


# now extract  and load json data

with open("api_users.json","r") as file:
     load_data =  json.load(file)


     for user in load_data:
             print("Name :", user["name"])
             print("Email :", user["email"])
             print("-" * 30)


