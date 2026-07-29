import os
import psutil
import sys
import smtplib
from email.message import EmailMessage


SENDER_EMAIL = "sagarbendale98@gmail.com"
SENDER_PASSWORD = "wwncafltlevbrkpu"


def CreateDirectory(dirname):

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    return os.path.join(dirname, "ProcessLog.txt")


def WriteProcess(file):

    file.write("Running Process Information\n\n")

    for process in psutil.process_iter(['pid', 'name', 'username']):

        try:

            file.write(f"Process Name : {process.info['name']}\n")
            file.write(f"PID          : {process.info['pid']}\n")
            file.write(f"Username     : {process.info['username']}\n")
            file.write("-----------------------------------\n")

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass


def SendMail(receiver, filepath):

    msg = EmailMessage()

    msg["Subject"] = "Running Process Report"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver

    msg.set_content("Please find attached process report.")

    file = open(filepath, "rb")
    data = file.read()
    file.close()

    msg.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename="ProcessLog.txt"
    )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    smtp.send_message(msg)
    smtp.quit()


def main():

    if len(sys.argv) != 3:
        print("Usage : python ProcInfoMail.py DirectoryName Email")
        return

    dirname = sys.argv[1]
    receiver = sys.argv[2]

    filepath = CreateDirectory(dirname)

    file = open(filepath, "w")

    WriteProcess(file)

    file.close()

    SendMail(receiver, filepath)

    print("Mail Sent Successfully")


if __name__ == "__main__":
    main()