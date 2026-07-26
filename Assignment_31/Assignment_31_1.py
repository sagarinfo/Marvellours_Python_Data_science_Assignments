import time
import schedule

def DisplayMessage(message):
    print(message)

def main():

    message = input("Enter message : ")
    interval = int(input("Enter interval in seconds : "))

    if interval <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(interval).seconds.do(DisplayMessage, message)

    print("Press Ctrl + C to stop the program.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()