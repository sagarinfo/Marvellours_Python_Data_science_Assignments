import os
import shutil
import time
from datetime import datetime

def main():

    source = input("Enter source directory : ")
    destination = input("Enter destination directory : ")

    if not os.path.isdir(source):
        print("Source directory does not exist.")
        return

    if not os.path.isdir(destination):
        print("Destination directory does not exist.")
        return

    while True:

        logfile = open("CopyLog.txt", "a")

        for file in os.listdir(source):

            if file.endswith(".txt"):

                src = os.path.join(source, file)
                dest = os.path.join(destination, file)

                try:
                    shutil.copy2(src, dest)

                    logfile.write(str(datetime.now()) + "\n")
                    logfile.write("Copied : " + src + "\n")
                    logfile.write("Destination : " + dest + "\n")
                    logfile.write("--------------------------------\n")

                    print(file, "copied successfully.")

                except Exception as e:
                    logfile.write(str(datetime.now()) + "\n")
                    logfile.write("Failed : " + src + "\n")
                    logfile.write("Reason : " + str(e) + "\n")
                    logfile.write("--------------------------------\n")

                    print("Unable to copy", file)

        logfile.close()

        print("Waiting for next cycle...")
        time.sleep(600)      # 10 minutes

if __name__ == "__main__":
    main()