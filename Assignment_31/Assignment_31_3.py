import os
import time
from datetime import datetime

def ScanDirectory(path):

    file_count = 0
    dir_count = 0

    for foldername, subfolders, filenames in os.walk(path):
        file_count = file_count + len(filenames)
        dir_count = dir_count + len(subfolders)

    print("\nDirectory Scanned :", path)
    print("Total Files :", file_count)
    print("Total Subdirectories :", dir_count)
    print("Scan Time :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

def main():

    path = input("Enter directory path : ")

    if not os.path.isdir(path):
        print("Directory does not exist.")
        return

    while True:
        ScanDirectory(path)
        time.sleep(60)

if __name__ == "__main__":
    main()