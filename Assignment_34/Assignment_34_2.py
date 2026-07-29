import psutil
import sys


def SearchProcess(ProcessName, file):

    found = False

    for process in psutil.process_iter(['pid', 'name', 'username']):

        try:

            if process.info['name'] is not None:

                if process.info['name'].lower() == ProcessName.lower():

                    found = True

                    file.write(f"Process Name : {process.info['name']}\n")
                    file.write(f"PID          : {process.info['pid']}\n")
                    file.write(f"Username     : {process.info['username']}\n")
                    file.write("------------------------------------\n")

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    if found == False:
        file.write("Process Not Found")


def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcInfo.py ProcessName")
        return

    ProcessName = sys.argv[1]

    file = open("ProcessInfo.txt", "w")

    file.write("Searching Process...\n\n")

    SearchProcess(ProcessName, file)

    file.close()


if __name__ == "__main__":
    main()