class ApiConfig:

            def __init__(self,api_key, model = "gpt 3.5 o turbo", max_tokens = 100):
                    
                    self.api_key= api_key
                    self.model = model
                    self.max_tokens = max_tokens
                    self.base_url = "https://api.openai.com/v1"


# now lets create an object

devConfig = ApiConfig("Azzzsfnvjsbfishasf",max_tokens="50")
                    

# now create another object and uses all positonal arguments


proConfig = ApiConfig("asfgasgsdgsdg",model="gpt-4",max_tokens="1000")

# now access the configuration thorugh .

print(devConfig.api_key)

print(proConfig.max_tokens)