import sys 
import os
import hashlib
import smtplib
import re
from datetime import datetime

def DisplayHelp():
    print("\n================ Duplicate File Removal Automation ================\n")
    print("Description:")
    print("This application scans a directory recursively,")
    print("identifies duplicate files using MD5 checksum,")
    print("deletes duplicate files, creates a log file,")
    print("and sends the log file through email.\n")

    print("Usage:")
    print("python DuplicateFileRemoval.py <DirectoryPath> <TimeIntervalInMinutes> <ReceiverEmail>\n")

    print("Arguments:")
    print("1. DirectoryPath          : Absolute path of directory")
    print("2. TimeIntervalInMinutes  : Time interval in minutes")
    print("3. ReceiverEmail          : Email address of receiver\n")

    print("Example:")
    print("python DuplicateFileRemoval.py E:\\Data\\Demo 30 abc@gmail.com")
    
def DisplayUsage():
    print("\nUsage:")
    print("python DuplicateFileRemoval.py <DirectoryPath> <TimeIntervalInMinutes> <ReceiverEmail>\n")

    print("Example:")
    print("python DuplicateFileRemoval.py E:\\Data\\Demo 30 abc@gmail.com")
    
    import sys

def ValidateArguments():

    if len(sys.argv) == 2:

        if sys.argv[1] in ("-h", "--help"):
            DisplayHelp()
            sys.exit()

        elif sys.argv[1] in ("-u", "--usage"):
            DisplayUsage()
            sys.exit()

        else:
            print("ERROR : Invalid option")
            DisplayUsage()
            sys.exit()

    elif len(sys.argv) != 4:
        print("ERROR : Invalid number of arguments")
        DisplayUsage()
        sys.exit()
import os

def ValidateDirectory(path):

    if path == "":
        return False

    if not os.path.isabs(path):
        print("ERROR : Please provide absolute path.")
        return False

    if not os.path.exists(path):
        print("ERROR : Directory does not exist.")
        return False

    if not os.path.isdir(path):
        print("ERROR : Given path is not a directory.")
        return False

    if not os.access(path, os.R_OK):
        print("ERROR : Directory cannot be accessed.")
        return False

    return True

def ValidateTimeInterval(interval):

    try:
        interval = int(interval)

        if interval <= 0:
            print("ERROR : Time interval should be greater than zero.")
            return False

        return True

    except ValueError:
        print("ERROR : Time interval should be numeric.")
        return False
    
def ValidateEmail(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True

    print("ERROR : Invalid Email Address.")
    return False            


def CreateLogDirectory():

    dirname = "Marvellous"

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    return dirname


def CreateLogFile():

    dirname = CreateLogDirectory()

    filename = "DuplicateRemovalLog_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".log"

    filepath = os.path.join(dirname, filename)

    return filepath

import hashlib

def CalculateChecksum(path):

    hashobj = hashlib.md5()

    try:

        with open(path, "rb") as file:

            while True:

                data = file.read(1024)

                if not data:
                    break

                hashobj.update(data)

        return hashobj.hexdigest()

    except Exception:
        return None
    
def ScanDirectory(path):

    files = []

    for FolderName, SubFolder, FileNames in os.walk(path):

        for file in FileNames:

            files.append(os.path.join(FolderName, file))

    return files

def FindDuplicateFiles(path):

    files = ScanDirectory(path)

    duplicate = {}

    for file in files:

        checksum = CalculateChecksum(file)

        if checksum is None:
            continue

        if checksum in duplicate:
            duplicate[checksum].append(file)
        else:
            duplicate[checksum] = [file]

    return duplicate

import os

def DeleteDuplicateFiles(duplicate):

    deleted_files = []

    for checksum in duplicate:

        if len(duplicate[checksum]) > 1:

            for file in duplicate[checksum][1:]:

                try:
                    os.remove(file)
                    deleted_files.append(file)

                except Exception as e:
                    print("Unable to delete :", file)

    return deleted_files

from datetime import datetime

def GenerateStatistics(path, duplicate, deleted_files, start_time):

    end_time = datetime.now()

    total_files = len(ScanDirectory(path))

    duplicate_count = 0

    for checksum in duplicate:
        if len(duplicate[checksum]) > 1:
            duplicate_count += len(duplicate[checksum]) - 1

    stats = {}

    stats["Start Time"] = start_time
    stats["End Time"] = end_time
    stats["Directory"] = path
    stats["Total Files"] = total_files
    stats["Duplicate Files"] = duplicate_count
    stats["Deleted Files"] = len(deleted_files)

    return stats

def WriteLog(logfile, stats, duplicate, deleted_files):

    with open(logfile, "w") as file:

        file.write("******** Duplicate File Removal Log ********\n\n")

        for key, value in stats.items():
            file.write(f"{key} : {value}\n")

        file.write("\nDeleted Files\n")
        file.write("-" * 60 + "\n")

        for item in deleted_files:
            file.write(item + "\n")

        file.write("\nDuplicate Files\n")
        file.write("-" * 60 + "\n")

        for checksum in duplicate:

            if len(duplicate[checksum]) > 1:

                file.write("\nChecksum : " + checksum + "\n")

                for name in duplicate[checksum]:
                    file.write(name + "\n")
                    
def CreateEmailBody(stats):

    body = ""

    body += "Duplicate File Removal Report\n\n"

    for key, value in stats.items():
        body += f"{key} : {value}\n"

    body += "\nLog file is attached."

    return body

import smtplib
from email.message import EmailMessage

def SendEmail(sender, password, receiver, logfile, body):

    try:

        msg = EmailMessage()

        msg["Subject"] = "Duplicate File Removal Report"

        msg["From"] = sender

        msg["To"] = receiver

        msg.set_content(body)

        with open(logfile, "rb") as file:
            data = file.read()

        msg.add_attachment(data,
                           maintype="application",
                           subtype="octet-stream",
                           filename=logfile)

        server = smtplib.SMTP("smtp.gmail.com",587)

        server.starttls()

        server.login(sender,password)

        server.send_message(msg)

        server.quit()

        print("Email Sent Successfully")

    except Exception as e:
        print("Unable to send email :",e)
        
from datetime import datetime

def PerformDuplicateRemoval(path, receiver):

    start_time = datetime.now()

    logfile = CreateLogFile()

    duplicate = FindDuplicateFiles(path)

    deleted_files = DeleteDuplicateFiles(duplicate)

    stats = GenerateStatistics(path,
                               duplicate,
                               deleted_files,
                               start_time)

    WriteLog(logfile,
             stats,
             duplicate,
             deleted_files)

    sender = "your_email@gmail.com"

    password = "your_app_password"

    body = CreateEmailBody(stats)

    SendEmail(sender,
              password,
              receiver,
              logfile,
              body)
    
import time

def Scheduler(path, interval, receiver):

    while True:

        print("Scanning Started...")

        PerformDuplicateRemoval(path, receiver)

        print("Next Scan After", interval, "Minutes")

        time.sleep(interval * 60)
       
import sys

def main():

    ValidateArguments()

    path = sys.argv[1]

    interval = sys.argv[2]

    receiver = sys.argv[3]

    if not ValidateDirectory(path):
        return

    if not ValidateTimeInterval(interval):
        return

    if not ValidateEmail(receiver):
        return

    Scheduler(path, int(interval), receiver)


if __name__ == "__main__":
    main()
    