# Strings

# We can declare in both ways strings in double quotes or single also

name = "Ahmad"

LastName = 'Malik'

paragraph = """
This is multiline String
to showcase the behaviour of multi line text
"""

print(paragraph)

# we can also concatenate the strings

first_Name = "Ahmad"
Last_Name = "Malik"

# Conatenation

full_Name = first_Name + " " + Last_Name

print(full_Name)

# Repetition

stars  = "*" * 6

age = "16" * 10

print(age) #repetetion in python strings

print(stars)

# You can also calculate the length of any string text 

fatherName = "Abdul" 

motherName = ""

print(len(fatherName))

print(len(motherName))

# we can also convert the integer numbers to strings

age2 = 21

# Now we convert the int to string

message = "I am " + str(age2) + " " + "Years Old"

print(message)
