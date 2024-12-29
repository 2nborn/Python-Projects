import os, shutil
path = r"C:/Users/User/Downloads/"
file_name = os.listdir(path)

folder_names = ["pbix files"]
for loop in range(0,1):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".pbix" in file and not os.path.exists(path + "pbix files/" + file):
        shutil.move(path + file, path + "pbix files/" + file)