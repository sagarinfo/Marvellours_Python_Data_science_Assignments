import schedule
import time
import datetime
import os

def Display():
    fobj = open("Marvellous.txt","a")
    
    fobj.write(f"Task excuted at : {datetime.datetime.now()} \n\n")
    print("file created")
def main():
    print("Automation Script Started")
    
    schedule.every(1).minutes.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print("End of Automation Script")
    
if __name__ == "__main__":
    main()    
    