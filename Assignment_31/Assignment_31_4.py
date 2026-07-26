import time
from datetime import datetime

def CreateLog():

    now = datetime.now()

    filename = "MarvellousLog_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    file = open(filename, "w")

    file.write("Log file created successfully.\n")
    file.write("Creation Time : " + now.strftime("%d-%m-%Y %I:%M:%S %p"))

    file.close()

    print(filename, "created successfully.")

def main():

    while True:
        CreateLog()
        time.sleep(600)      # 10 minutes

if __name__ == "__main__":
    main()