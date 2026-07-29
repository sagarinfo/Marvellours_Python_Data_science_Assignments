import psutil


def CreateLogFile():
    file = open("ProcessLog.txt", "w")
    file.write("********** Running Process Information **********\n\n")
    return file


def DisplayProcessInfo(file):

    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            file.write(f"Process Name : {process.info['name']}\n")
            file.write(f"PID          : {process.info['pid']}\n")
            file.write(f"Username     : {process.info['username']}\n")
            file.write("-----------------------------------------\n")

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass


def main():

    try:
        file = CreateLogFile()

        file.write("Automation Script Started\n\n")

        DisplayProcessInfo(file)

        file.write("\nAutomation Script Finished Successfully")

        file.close()

    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()