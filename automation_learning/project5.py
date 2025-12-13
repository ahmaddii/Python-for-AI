import csv
from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
        soap = BeautifulSoup(response.text,"html.parser") # get text only and html pareser understnd the code of website
else:
        print("Failed to fetch data from URL")

quotes = soap.find_all("span",class_="text") # find classes with text only and span tags find all through soap

# now create file and save data in it 


with open("quotes2.csv","w",newline="") as file:
           writer_data = csv.writer(file) # create csv file
           writer_data.writerow(["Quotes from website"]) # column header name
           print("File Created Succesfully !")
           count = 0

           for quote in quotes:
                   writer_data.writerow([quote.text]) # write on new row of which ever quote comes in only text
                   count += 1

print(f"Total Quotes Scraped is {count}")