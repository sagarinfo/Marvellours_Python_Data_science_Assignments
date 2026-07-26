import os
import time
from datetime import datetime

def main():

    filename = input("Enter file path : ")

    while True:

        log = open("FileSizeLog.txt", "a")

        if os.path.exists(filename):

            size = os.path.getsize(filename)

            log.write("Date & Time : " + str(datetime.now()) + "\n")
            log.write("File Path : " + filename + "\n")
            log.write("File Size : " + str(size) + " Bytes\n")
            log.write("-------------------------------------\n")

            print("Information Logged Successfully.")

        else:

            log.write("Date & Time : " + str(datetime.now()) + "\n")
            log.write("Error : File does not exist.\n")
            log.write("-------------------------------------\n")

            print("File does not exist.")

        log.close()

        time.sleep(30)

if __name__ == "__main__":
    main()