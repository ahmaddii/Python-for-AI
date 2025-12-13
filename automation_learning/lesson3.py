import json

data = {

            "name": "Ahmad",
            "email": "malik@gmail.com",
            "skills": ["automation","flutter"]

}

# created and write a data inside json file

with open("user.json","w") as file:
            json.dump(data,file,indent=4)


# now we have to read the json data 

with open("user.json","r") as file:
        
     user =  json.load(file)

     # apply check for read worlds

     if "automation" in user["skills"]:
             print("User is Eligible for Automation Tasks")

print(user)