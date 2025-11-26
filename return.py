# if you want some result to be return after function

def add(a,b):
           return a+b #it returns a + b


result = add(4,5)

print(result)

def calculateArea(width,height):
        area = width*height
        return area


result = calculateArea(24,39)

print(f"The Room Area is {result} Sq Feet")


# Return values used in many ways

def double(number):
        return number * 2


total = double(4) + double(5) # so we call two type functions and then add them to give total


print(total)


# you can also return multiple values like

def min_max_value(numbers):
        return min(numbers) , max(numbers)

# from list we get min or max values

min,max = min_max_value([2,3,4,6,10])

print(f"Min Value is : {min} and Max Value is {max}")

# now we can also get from tuple

#tuple_value = min_max_value([2,4,5,10])

#print(tuple_value)

def greeting_return(name):
        return print(f"Hello {name}")

greeting_return("Ahmad")

#print(message.upper())


