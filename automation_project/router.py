import csv

from config import MOTIVATIONAL_FILE,PHILOSOPHICAL_FILE,TECH_FILE

def route_quote(quote,category):

            file_map = {
                    
                    "Technical": TECH_FILE,
                    "Motivation": MOTIVATIONAL_FILE,
                    "Philosify": PHILOSOPHICAL_FILE
            
            }

            file_path  = file_map.get(category)

            if file_path:
                    with open(file_path,"a",newline="",encoding="utf-8") as file:
                        writter   = csv.writer(file)
                        writter.writerow([quote])