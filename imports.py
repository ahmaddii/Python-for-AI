import random
import datetime
import os
import json
import requests
import pandas as pd

# methods of imports 

import math # ya whole module import krlo

from math import sqrt,pi # ya to phir sqrt or pi iss ko import krlo

number = random.randint(1,10)

print(number)

text = random.choice(["orange","bluberry","watermelon"])

print(text)

today = datetime.date.today()

today2 = datetime.time.hour
print(today2)
print(today)

current_dir = os.getcwd()

print(current_dir)

data = {"name": "ahmad","age": 14}

json_string = json.dumps(data)

print(json_string)


result = sqrt(16)



print(result)


x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)



data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}

print(type(data))

df = pd.DataFrame(data)

print(df)