import os

print("Current Dirctory",os.getcwd())  # current dirctory

data_path = "data/sales.csv"

if os.path.exists(data_path):
            print(f"Path Finded  {data_path}")

else:
        print(f"Dosent Find the path {data_path}")
        print("Plz Ensure you are in the right Dirctory")


# just created a script to find path of file or folder exists or not