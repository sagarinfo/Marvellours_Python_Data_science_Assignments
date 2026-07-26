import time
import schedule

def DisplayMessage(message):
    print(message)

def main():

    message = input("Enter message : ")

    schedule.every(5).seconds.do(DisplayMessage, message)

    print("Message will be displayed every 5 seconds.")
    print("Press Ctrl + C to stop the program.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()