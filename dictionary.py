my_dic = {} # Empty dictionary jis mein abhi koi data ni dala


# dictionary data ke sath

person = {

"name": "Ahmad",
"age": 19,
"City": "Mianwali"

}

# now how can you acces the key data

print(person["name"])

print(person["City"])

print(person.get("name")) # .get ke through bhi kr skte hain values ko get


# some other way to store data in dictionary

scores = dict(math=90 , physics = 20) # 3rd way to declare a dictionary


# you can also put changes in dictionary like update or add some thing new data

# like 

person["email"] = "malikahmad@gmail.com"

print(person)

person["age"] = 20

print(person)

del person["email"]

print(person)

#person.clear()

print(person)

# some methods on dict

print(person.keys())

print(person.values())

print(person.items())

# we can also check if the key in dicto exists

if "name" in person: {

print("Found")

}
            
            # if you want multiple data to update in dict

person.update({"age": 50, "City": "Isb"})

print(person)


# Nested dictonireas

students = {


 "ahmad": {"age":20 , "grade": "A"},
 "Ali": {"age": 51, "grade": "B"},
 "Fahad": {"age": 21, "grade": "C"}


}

print(students)

print(students["ahmad"]["grade"])

print(students["Fahad"]["age"])