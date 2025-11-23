empty_set = set()

print(type(empty_set))

#From a list removes the duplicate data

scroes = [12,12,34,34,20,80]

unique_Scores = set(scroes)

print(unique_Scores)

#basic operations 

colors = {"red","blue","gree"}

print(type(colors))

colors.add("yellow")

print(colors)

#colors.remove("blue") # error if not found
#colors.remove("blue") # cant give error

if "red" in colors: {

print("Available")

}

# main uses is to remove duplicate items

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

unique_name = list(set(names))

print(unique_name)

allowed_users = {"alice","bob"}

if "alice" in allowed_users: {

            print("access granted")
}

