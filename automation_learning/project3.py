import json


# uses list for mutiple users

data = [

            {

            "name": "ahmad",
            "email": "malik@gmail.com",
            "skills": ["automation","flutter","python"]

            },
            
            {

            "name": "ali",
            "email": "ali@gmail.comn",
            "skills": ["javascript,react"]

            }

]

with open("users.json","w") as file:

            json.dump(data,file,indent=4)


# now read the file

with open("users.json","r") as file:
        
       load_Data = json.load(file)

       for user in load_Data:
               if "python" in user["skills"]:
                       print(f'Python Developer Found with Email is {user["email"]} and name is {user["name"]}')
            

print(load_Data)

