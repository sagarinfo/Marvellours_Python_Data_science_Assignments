import os
import time
from datetime import datetime

def CountFiles(path):

    count = 0

    for foldername, subfolders, filenames in os.walk(path):
        count = count + len(filenames)

    logfile = open("DirectoryCountLog.txt", "a")

    logfile.write("Directory Path : " + path + "\n")
    logfile.write("Number of Files : " + str(count) + "\n")
    logfile.write("Date & Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    logfile.write("----------------------------------------\n")

    logfile.close()

    print("Total Files :", count)

def main():

    path = input("Enter directory path : ")

    if not os.path.isdir(path):
        print("Directory does not exist.")
        return

    while True:
        CountFiles(path)
        time.sleep(300)      # 5 minutes

if __name__ == "__main__":
    main()