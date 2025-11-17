# JOining or Concatenation of strings

first_Name = "Ahmad"
Last_Name = "Rasheed"

full_Name = print(first_Name + " " +  Last_Name)

greeting = print(f"Hello {first_Name}")

# If you want repetions 

star = "*"

stars = star * 20
print(stars)


# Convert cases of different strings

text = "Python Programing"

print(text.lower()) # methods
print(text.upper())
print(text.title())

# how we can clean a strings

messy = "   Hello World    "
print(messy.strip()) # it just removes the whtie spaces

price = "$19.99"

print(price.strip("$"))

message = "Hello I am malik ahmad learning Python with AI ML"

# check if something exists

print("Python" in message) # true
print(message.startswith("Hello")) # true
print(message.endswith("hello")) # false


# Find position

print(message.find("Python")) # occur at 32 

print(message.count("Python"))


new_message = message.replace("Python" , "Javascript")
print(new_message)