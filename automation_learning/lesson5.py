import requests
from bs4 import BeautifulSoup
import csv


url = "https://quotes.toscrape.com/"

response = requests.get(url)

soap = BeautifulSoup(response.text , "html.parser")

quotes = soap.find_all("span", class_="text")

# now run loop


# now paste in csv

with open("quotes.csv","w",newline="") as file:
        
       writter = csv.writer(file)
       writter.writerow(["Quotes"])

       for quote in quotes:
              writter.writerow([quote.text])


print("CSV FILE SAVED")
               