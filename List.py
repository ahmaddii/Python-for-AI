# Lists

my_List = [] # Empty list bna di ha 

fruites = ["banna","grapes","watermelon"] # indexing per hi store hota ha start hogi from 0

print(fruites)

numbers = [1,2,3,4,5]

mixed = ["banna",23,"grapes"]

print(mixed) # krskte hain

# if you want to access any list element just type its index number

print(fruites[0]) # in postive index it goes from left to right 

print(fruites[-1]) # and in negative it goes from right to left 

print(fruites[0:2]) # slicing
print(fruites[1:])

# list are mutable you can change them

fruites[0] = "strawberyy"

print(fruites)

# you can also add items in the list 

fruites.append("Mango") 
print(fruites) # it add mango at last of string

fruites.insert(5,"chacha")

print(fruites)

# you can also delete or remove any item in the list

fruites.remove("grapes")
print(fruites)

last = fruites.pop()

print(last) # akhri element pop how ha to wo last mein store pop or return krega

print(fruites)

del fruites[0]

print(fruites)

# Methods you can perform on list 

numbers = [1,2,3,4,5,5,2]

print(len(numbers)) # get length of list
print(numbers.count(1)) # check how many times specific thing come
print(numbers.index(2)) # kis index per 2 pera howa ha 

numbers.sort() # chote se bara method hota ha 

print(numbers)

numbers.reverse()

print(numbers)

copyList = numbers.copy() # creates a copy of my list of numbers 

print(copyList)

# you can check the lists by if else 


if "banna" in fruites:
            print("banna is available")


if fruites:
        print("List is full")

else:
        print("List is emptys")


# Wrong - both variables point to same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - changed!
print(list2)

# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy() # its a shallow copy issues
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged
print(list2)