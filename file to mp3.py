import os
path = input("enter path to folder containing files.")
files = os.listdir(path)
print(files[0])
print(files)
for i in files:
    os.rename(path+i, path+i+".mp3")




