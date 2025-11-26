import requests

latitude = 48.9
longitude = 2.8


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url) # url se data le kr response ke ander rakaha

data = response.json() # response ko json format mein krdiya convert for readb,ity

print(data)



def get_weather(longitude,latitude):
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
            data = response.json()

            return data['current']['temperature_2m']


paris_temp = get_weather(28.9,14.8)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris Temp is : {paris_temp}")