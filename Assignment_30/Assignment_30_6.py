"""
Task 6: Schedule two daily tasks using the `schedule` library.
Install dependency first:  pip install schedule
"""

import schedule
import time


def print_lunch_time():
    print("Lunch Time!")


def print_wrap_up_work():
    print("Wrap up work")


def main():
    schedule.every().day.at("13:00").do(print_lunch_time)   # 1:00 PM
    schedule.every().day.at("18:00").do(print_wrap_up_work)  # 6:00 PM
    print("Scheduler started. Waiting for scheduled tasks... (Ctrl + C to stop)")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()