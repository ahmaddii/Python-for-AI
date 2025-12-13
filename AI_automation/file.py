with open("file.txt","w") as file: # open file file.txt 
            file.write("Learning AI automation") # and write this text inside it


# append method very common in automation

with open("file.txt","a") as file:
        file.write("\nNew Automation Task have Added")

# now there is also read method for a file handling

with open("file.txt","r") as file:
      content = file.read()

print(content)