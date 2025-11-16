# Operaters in Python how we talk or to communicate between data

print(3 + 5) 
print(3 - 5)
print(3 * 5)
print(3 / 5)
print(3 % 5) # remainder ya modulo

print(3 ** 5) # power
print(3 // 5) # round off


result1 = 3 + 4 * 5 # so it starts from right most so first it do 5 * 4 = 20 + 3 = 23 not 35

print(result1) # so = 23 not 35

# similarly if we want from left or any other side and want braces or parenthesis operationsd one first

result2 = (3 + 4) * 5

print(result2)

age = 25
has_Licensed = True

# in And both have to true then answer is true

can_drive = age >= 18 and has_Licensed
print(can_drive)

day = "Saturday"

# Only one is true it gives true 

is_Weekend = day == "Saturday" or day == "Sunday"
print(is_Weekend)

print(not True)

# Assignment operaters

score = 10

# score = score + 10

score += 20

print(score)

# works with all other operaters like -= or *= or /= 