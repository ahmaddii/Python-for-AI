# Methods and attributes in classes

# two types of attributes first is instance attributes which are uniqiye to every client or object


class ApiConfig:

            version = "1.1" # class attributes shared among all objects or clients 
            module = "gpt-4"

            def __init__(self,api,base_url):
                    
                    self.api = api
                    self.base_url = base_url
                    self.request = 0

# now creates objects

dg1 = ApiConfig("safgasfas","www.google.com")

dg2 = ApiConfig("asagsgs","www.fax.com")


print(dg1.base_url)

print(dg2.base_url)

print(dg2.version)

print(dg1.version)

# so every attribute has its own url unique 


# class attributes

# which are delcare in class 
            
                    