class Animal:

            def __init__(self,name):
                    self.name = name

            def eat(self): # Eating
                    return print(f"{self.name} is Eating")
            
            def sleeping(self): # Sleeping
                    return print(f"{self.name} Sleeping")
            
            def makeSound(self):
                    return print(f"{self.name} makes some sound as well")
            

            # So child class can override the methods inside the parent class with same name

class Dog(Animal):
        
        def bark(self):
                return print(f"{self.name} is Barking")
        
        def makeSound(self): # so this method overide the parent method so it print this message of woofing instead of its parent one
                return print(f"{self.name} is Woofing.......")
        
# now create objects of Dog class

my_Dog = Dog("Bully")

my_Dog.makeSound()


my_Dog.eat()
my_Dog.sleeping()
my_Dog.bark() # you can do it with positional argument and also name argument as well