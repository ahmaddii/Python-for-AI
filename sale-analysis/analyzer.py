import pandas as pd
import os
import json
from helpers import calculate_total,format_currency

df = pd.read_csv("data/sales.csv")
print("Csv Data")
print(df)

print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} column")


totals = []

for index,row in df.iterrows():
            total = calculate_total(row["quantity"],row["price"])
            totals.append(total)

df["total"] = totals

print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")


# calculat total for each row

#df["total"] = df["quantity"] * df["price"]
#print("\nWith totals:")
#print(df)

# now make output dirctory

os.makedirs("output",exist_ok=True)

# now store the data into multiple files

df.to_json("output/sales_analysis.json",orient='records',indent=2)

df.to_csv("output/sales_analysis.csv",index=False)

df.to_excel("output/sales_analysis.xlsx",index=False)

print("\nFiles Saved")
print("- output/sales_analysis.json")
print("- output/sales_analysis.xlsx")
print("- output/sales_analysis.csv")








#import os

#print("Current Dirctory",os.getcwd())  # current dirctory

#data_path = "data/sales.csv"

#if os.path.exists(data_path):
 #           print(f"Path Finded  {data_path}")

#else:
       # print(f"Dosent Find the path {data_path}")
        #print("Plz Ensure you are in the right Dirctory")


# just created a script to find path of file or folder exists or not