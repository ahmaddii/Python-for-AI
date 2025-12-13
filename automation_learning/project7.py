import requests
import csv
from bs4 import BeautifulSoup
import google.generativeai as genai

url = "https://quotes.toscrape.com/"


response = requests.get(url)


if response.status_code == 200:
            soap = BeautifulSoup(response.text,"html.parser")

else:
        print("Failed to fetch data using soap")


quotes = soap.find_all("span",class_="text")


with open("web-scrap.csv","w",newline="") as file:
      writter = csv.writer(file)
      writter.writerow(["Simple Quotes"])

      for quote in quotes:
              writter.writerow([quote.text])

print("File saved")

genai.configure(api_key=API_KEY)

# selct model

model = genai.GenerativeModel("gemini-2.5-flash")


prompt = f"Classify these quote as motivational, philosophical, or technical {quotes}"

response = model.generate_content(prompt)

with open("ai_response2.txt","w") as file:
        file.write(response.text)
        print("File Created--")