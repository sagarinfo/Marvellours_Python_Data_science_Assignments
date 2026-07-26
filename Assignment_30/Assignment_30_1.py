import schedule
import time
import datetime

def Display():
    print("Jay Ganesh....")

def main():
    print("Automation Script Started")
    
    schedule.every(2).seconds.do(Display)
    
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    print("End of Automation Script")
    
    
if __name__ == "__main__":
    main()    
    