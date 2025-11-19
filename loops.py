# without loop for 5 times hello world

print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")


for i in range(5):
            print("Ahmad")


for i in range(10): # so its starts from zero so we can say it is called zero indexing in python
        print(i)


# count from different starting points 


for i in range(1,6): # give the two inputs starting point and ending point
        print(i)

# if you want some kind of gap like 2s or 3s you can do

for i in range(1,10,2):
  print(i)


# you can also loop through a text like

name = "Ahmad"

for letter in name:
        print(letter)

# we can also print evry data from the list item as well how

colors = ["Red", "Blue" , "Yellow"]

for color in colors:
        print(f"I Like {color}")

# while loop runs until condition is true

count = 0

while count <=5:
        print(f"count is {count}")
        count = count + 1