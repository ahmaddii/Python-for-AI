# declare the function

price = 100 # Global Scope Access

def greet():
            print("Hello World")
            print("Welcome to Python")

greet()
greet()

def check_wheather():
        temp = 25

        if temp >= 25:
                print("Its Hot")
        else:
                print("Its Cold")
                

check_wheather()

# Local Variables cant be access outside the function

def calculate_Total():
      #  price = 100  block scope

      # if you want to make the local variable global just write

    #  global price = 200

        tax = price * 0.1
        print(f"Total Amount is : {price + tax}")



print(price)

calculate_Total()


def total(amount):
       
        global total 
        total = 0
        total += amount
        return total


total(20)
print(total(20))

print(total)

