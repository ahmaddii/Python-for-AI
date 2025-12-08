 #try:
            # code which have possibliy of error
 #           riskey_operation()

#except:
       # print("Something Went wrong") # if error occurs then it comes to except block



try:
            age = int(input("Enter your age"))
            print(f"After 10 Years Your age is {age + 40}")

except ValueError:
        print("Enter valid value for age")
        

# there are multiple error types


try:
        with open("numbers.txt","r") as f:
                text = f.read()
                number = int(text)
                result = 100 / number
                print(f"Result {result}")

except FileNotFoundError:
        print("File Not found")

except ValueError:
        print("File dosent have valid value")

except ZeroDivisionError:
        print("Cant divide with zero")


# The else clause runs if no error occurs

try:
        with open("numbers.txt","r") as f:
                data = f.read()

except FileNotFoundError:
        print("File not found")

else:
        print(f"The data length is {len(data)}")


# now comes finally clause in error handling it always runs if error happens or not

try:
        with open("numners.txt","r") as f:
                data = f.read()

except FileNotFoundError:
        print("File not exist")

finally:
        # this always runs to complete the clean up
        if 'f' in locals and not f.closed():
                f.close()
                print("Clean Up complete") 