
def greet(name,age):
            print(f"Name is {name} and age is {age}")



greet("ahmad",16)
greet("ali",20)

def calculate_Total(price,taxRate,discount):
        tax = price * taxRate
        final_price = price + tax - discount
        print(f"Total Bill is : {final_price} tax is {tax} and discount is {discount}")


calculate_Total(1200,12,100)

# default values to paranetrs

def hello(name , greetings="hello"):
        print(f"{greetings} , {name}" )


hello("ahmad")