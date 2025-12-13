import csv

with open("leads2.csv","w") as file:

       writer  =  csv.writer(file)

       writer.writerow(["Name", "Email", "Company"])

       writer.writerow(["Ahmad", "malik@gmail.com", "google"])
       writer.writerow(["Ali", "m@gmail.com", "google"])
       writer.writerow(["Hassan", "malik@pulxar.com", "google"])

# now read the file

with open("leads2.csv","r") as file:
       
      reader = csv.reader(file)

      for row in reader: # apply the filter on csv with gmail email only needed
             if "gmail" in row[1]:
                    print("Gmail Leads",row)