
age = 20

score = 30  # numbers without decimal points

# number with decimal points


age2 = 20.555

score = 3.1555


# basic operations with numbers 


num1 = 12

num2 = 15

add = num1 + num2 

sub = num1 - num2

div = num1 / num2

module = num1 % num2

square = 2 ** 2 # for square of any number

cube = 2 ** 3 # for cube 


print(cube)

# integer vs float division 

integer = 10 / 3  # gives 3.333333333

print(integer)

# so we have to round it up using // 

integer2 = 10 // 3

print(integer2)


# even if you are diving with even check it any zero left on right so round it up

result = 10 / 2 # so gives 5.0

print(type(result)) # its type is float ok we need regular integer

print(result) 

# so round it up

result2 = 10 // 2

print(result2) # So now its converted to fully integer so you need to avoid these mistakes

print(type(result2))


# , means = type 
# . means = number so remeber

numb = 10_000_0000 #python style

print(numb)