import os
import shutil

path = input("Enter path :")

files = os.listdir(path)

for i in files:
    file_name , exatantion = os.path.splitext(i)
    final_extantion = exatantion[1:]

    if os.path.exists(path+"\\"+final_extantion):
        shutil.move(path+"\\"+i , path+"\\"+final_extantion+"\\"+i)
    else:
        os.makedirs(path+"\\"+final_extantion)
        shutil.move(path+"\\"+i , path+"\\"+final_extantion+"\\"+i)
