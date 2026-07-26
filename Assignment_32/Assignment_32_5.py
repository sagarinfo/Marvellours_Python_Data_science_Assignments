import os
import time
from datetime import datetime

def main():

    directory = input("Enter directory path : ")

    if not os.path.isdir(directory):
        print("Directory does not exist.")
        return

    while True:

        logfile = open("DeleteLog.txt", "a")

        for foldername, subfolders, filenames in os.walk(directory):

            for file in filenames:

                filepath = os.path.join(foldername, file)

                try:

                    if os.path.getsize(filepath) == 0:

                        os.remove(filepath)

                        logfile.write(str(datetime.now()) + "\n")
                        logfile.write("Deleted : " + filepath + "\n")
                        logfile.write("--------------------------------\n")

                        print(filepath, "deleted.")

                except PermissionError:

                    logfile.write(str(datetime.now()) + "\n")
                    logfile.write("Permission Denied : " + filepath + "\n")
                    logfile.write("--------------------------------\n")

                    print("Permission denied:", filepath)

                except Exception as e:

                    logfile.write(str(datetime.now()) + "\n")
                    logfile.write("Error : " + str(e) + "\n")
                    logfile.write("--------------------------------\n")

        logfile.close()

        print("Waiting for next scan...")
        time.sleep(3600)      # 1 hour

if __name__ == "__main__":
    main()