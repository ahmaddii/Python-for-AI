from datetime import datetime
from config import LOG_FILE


# for success print this log on the file

def log_info(message):
            with open(LOG_FILE,"a") as file:
                    file.write(f"[INFO] {datetime.now()} - {message}\n")


       # for error print this log in the file      

def log_error(message):
        with open(LOG_FILE,"a") as file:
                file.write(f"[ERROR] {datetime.now()} - {message}\n")