class DataValidater:

            def __init__(self):
                    
                    self.errors = []

            def validate_email(self,email):
                    
                    if "@" not in email:
                            self.errors.append(f"Invalid Email : {email}")
                            return False
                    return True
            
            def validate_age(self,age):
                    
                    if age < 0 and age > 150:
                            self.errors.append(f"Inavlid age : {age}")
                            return False
                    return True
            

            def get_errors(self):
                    
                    return self.errors
                    

validater1 = DataValidater()

#svalidater1.validate_email(email="malik")
validater1.validate_age(age=300)

print(validater1.get_errors())

print(validater1.get_errors())