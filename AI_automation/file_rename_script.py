import os

folder_path = "/home/malikahmadrasheed/Downloads/test_files"

for count,filename in enumerate(os.listdir(folder_path), start=1):
            file_extention = os.path.splitext(filename) # get file extention from after .
            new_name = f"image_{count}.{file_extention}"
            
            old_path = os.path.join(folder_path,filename)
            new_path = os.path.join(folder_path,new_name)

            os.rename(old_path,new_path)

print("Renaming Complelte--")


