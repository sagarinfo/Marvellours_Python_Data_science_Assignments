import os
import psutil
import sys


def CreateDirectory(dirname):

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filepath = os.path.join(dirname, "ProcessLog.txt")

    return filepath


def WriteProcessInfo(file):

    file.write("Running Process Information\n\n")

    for process in psutil.process_iter(['pid', 'name', 'username']):

        try:

            file.write(f"Process Name : {process.info['name']}\n")
            file.write(f"PID          : {process.info['pid']}\n")
            file.write(f"Username     : {process.info['username']}\n")
            file.write("---------------------------------\n")

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass


def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcInfoLog.py DirectoryName")
        return

    dirname = sys.argv[1]

    filepath = CreateDirectory(dirname)

    file = open(filepath, "w")

    WriteProcessInfo(file)

    file.close()

    print("Log File Created Successfully")


if __name__ == "__main__":
    main()