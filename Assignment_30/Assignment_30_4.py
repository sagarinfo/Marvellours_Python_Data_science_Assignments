import schedule
import time
import datetime

def Display():
    print("Namskar....")

def main():
    print("Automation Script Started")
    
    schedule.every().day("9:00").do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print("End of Automation Script")
    
if __name__ == "__main__":
    main()    
    