import os

current_dir = os.getcwd()

for folder, sub_folder, files in os.walk(current_dir):
    print(folder, sub_folder, files)

print("*****")

for folder, sub_folder, files in os.walk(current_dir):
    for file in files:
        print(folder + "\\" + file)
