import time
from datetime import datetime

def main():

    while True:
        now = datetime.now()

        filename = "File_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

        file = open(filename, "w")

        file.write("Filename : " + filename + "\n")
        file.write("Creation Date : " + now.strftime("%d-%m-%Y") + "\n")
        file.write("Creation Time : " + now.strftime("%H:%M:%S") + "\n")

        file.close()

        print(filename, "created successfully.")

        time.sleep(60)

if __name__ == "__main__":
    main()