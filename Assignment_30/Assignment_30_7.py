"""
Task 7: Perform a file backup every hour.

- Accepts a source file path and a destination directory path.
- Copies the source file to the destination directory.
- Appends the current date/time to the backup filename.
- Logs each backup operation into backup_log.txt.
"""

import os
import shutil
import time
from datetime import datetime

LOG_FILE = "backup_log.txt"


def backup_file(source_path: str, destination_dir: str) -> None:
    """Copy source_path into destination_dir with a timestamped filename,
    then log the operation."""
    if not os.path.isfile(source_path):
        print(f"Error: Source file '{source_path}' does not exist.")
        return

    os.makedirs(destination_dir, exist_ok=True)

    now = datetime.now()
    name, ext = os.path.splitext(os.path.basename(source_path))

    # Example: Data_25_07_2026_16_30_00.txt
    name_timestamp = now.strftime("%d_%m_%Y_%H_%M_%S")
    backup_filename = f"{name}_{name_timestamp}{ext}"
    destination_path = os.path.join(destination_dir, backup_filename)

    shutil.copy2(source_path, destination_path)

    # Example: Backup completed successfully at 25-07-2026 04:30:00 PM
    log_timestamp = now.strftime("%d-%m-%Y %I:%M:%S %p")
    log_entry = f"Backup completed successfully at {log_timestamp}\n"

    with open(LOG_FILE, "a") as log:
        log.write(log_entry)

    print(f"Backup created: {destination_path}")
    print(log_entry.strip())


def run_hourly_backup(source_path: str, destination_dir: str) -> None:
    """Repeat the backup every hour, forever."""
    while True:
        backup_file(source_path, destination_dir)
        time.sleep(3600)  # 1 hour
def main():
    src = input("Enter the source file path: ").strip()
    dest = input("Enter the destination directory path: ").strip()
    run_hourly_backup(src, dest)

if __name__ == "__main__":
    main()