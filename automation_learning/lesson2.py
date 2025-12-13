import csv

with open("leads.csv","w",newline="") as file:

       writer =  csv.writer(file) # write a csv data in file leads .csv

       writer.writerow(["Name" , "Email" , "Company"])

       writer.writerow(["Ahmad", "malik@gmail.com", "PuslarX"])
       writer.writerow(["Ali", "ali@gmail.com", "google"])

print("Csv File Created Successfully !")


# now how to read the file simple as we done earlier

with open("leads.csv","r") as file:
       
     reader = csv.reader(file) # read the file method of csv

     for row in reader:
           print(row)

