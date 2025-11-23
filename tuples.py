
# creating tuples

# tuples are immutable

empty = () # emoty tuple


# tuple with items 

point = (5,6)

print(point)

colors = ("red" , "blue","black")

print(colors)

# single item store in tuple using , otherwise python thinks it just parenthesse

item = (42,)

print(item)

print(type(item))

coordinates = 20,40 # without parenthesis

print(coordinates)

print(colors[2])

print(colors[-2])

# you can also do slicing

print(colors[0:2]) # 0 to 1

# you can also unpacke the tuples

points = (5,4)

x,y = points # means x now = 5 and y = 4 it is coolest feature of tuple in python unpacking the tuples

print(x,y)


# Also swap them

x,y = y,x

print(x,y)
print(y,x)


# main difference between tuples are list are list are mutable and same as dictionary and tuple are immutable