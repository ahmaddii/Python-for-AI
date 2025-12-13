with open("automation_log.txt","w") as file:
            file.write("Automation Started")

with open("automation_log.txt","a") as file:
        file.write("\nToday Iis 13 Dec 2025")
 

with open("automation_log.txt","r") as file:
      content = file.read()

print("==File Created==")
print(content)