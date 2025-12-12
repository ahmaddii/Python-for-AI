# Question 1 for basic Input

name,age,city = "Ahmad",21,"Mianwali"

print(f"My Name is {name} and my age is {age} and my city is {city}")


# Question 2 

print("Enter Number 1 ")

number1 = input()

print("Enter Number 2 ")

number2 = input()

sum = int(number1) + int(number2)

print(sum)

# Question 3

print("Enter User Age")

age = input()

if int(age) < 12:
            print("Child")
elif int(age) >=13 and int(age) <=19:
        print("Teenager")
else:
        print("Adult")
        

# Question 4

maths = 42
physics = 50
chemistry = 19

avg = (maths + physics + chemistry) / 3

print(avg)


sentence = "My name is Ahmad"

print(len(sentence)) # characters
print(sentence.split()[0])  # first word
print(sentence.split()[3]) # last word


# Part B

# Question 1

#for i in range(1,21):
   #     print(i)


# Question 2

inputNumber = input("Enter the Number for Multiplication")

number = int(inputNumber) # convert string to int

print("----------Multiplication Table for Given Number is------ ")

for i in range(1,11):
        
        result = number * i
        print(f"{number} * {i} = {result}")

# Queston 3 to check the even count from 1 to 50

count = 0 # inital zero even number

for number in range(1,51):
        
        if number % 2 == 0:
                count += 1
print(f"Total Even numbers are {count}")


# Question 4 for print each list item with the help of for loop

colors = ["red", "blue", "green", "yellow"]

for i in colors:
        print(i)


for i in reversed(range(1,31)):
        print(i)

# functions 


def add(a,b):
        return a+b



sum = add(1,4)
print(sum)


def is_even(n):
        if n % 2 == 0:
                print("True Even")
        else:
                print("Odd")


print(is_even(3))
print(is_even(5))


def largest_number(numbers):
        
        if not numbers:
                return None
        return max(numbers)

# now create a list

my_list = [12,24,55,22,18,1]

largest = largest_number(my_list)

print(f"Largest Number is {largest}")



def print_name(name):
        
        print(f"Hello,{name}")

namee = print_name("ahmad")

print(namee)
        

