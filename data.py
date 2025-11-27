import requests
from datetime import datetime,timedelta
import json
import pandas as pd
import matplotlib.pyplot as plt
import os


today = datetime.now() # tell us about todays date and time

# now we want a prevoius week  date and time

week_ago = today - timedelta(days=7) # pichle 7 dinon ka

# format the start of end date of the week with respect to api

start_date = week_ago.strftime("%Y-%m-%d") # and start from prevous week
end_date = today.strftime("%Y-%m-%d") # end day is today

# get data through api for start or end date for paris of past week

url = f"https://api.open-meteo.com/v1/forecast?latitude=33.684422&longitude=73.047882&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
 
response = requests.get(url) # get data from url and save it in response 

data = response.json() # and then convert that response to json and save it to data

print(json.dumps(data,indent=4))


# now we use pandas pkg to load that data into csv format rows column

daily_data = data["daily"]

# now we create a dataframe

df = pd.DataFrame({

            "date": daily_data["time"],
            "max_temp": daily_data["temperature_2m_max"],
            "min_temp": daily_data["temperature_2m_min"]

})

print(df)


# now lets create a plot to visulize the things

plt.figure(figsize=(10,6))
plt.plot(df["date"],df["max_temp"],marker = 0,label = 'Max Temp')
plt.plot(df["date"],df["min_temp"], marker = 0, label= "Min Temp")

# Add labels and title

plt.xlabel("Date") # x axis
plt.ylabel("Temperature C") # y axis
plt.title("Islamabad Temperature - 7 days")
plt.legend()


# rotate x axis to 45 degree for readbility

plt.xticks(rotation=45)
plt.tight_layout()

# now save the plot and show 

plt.savefig("weather-fig.png")
#plt.show()

# now for later use we need to store the data into csv file so lets do it

if not os.path.exists("data"):
            os.mkdir("data")

# now save to csv the df data frame data

df.to_csv("data/weather_data.csv",index=False)
print("Csv File is saved in data/weather_data.csv")