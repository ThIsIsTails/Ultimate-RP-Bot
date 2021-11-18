import colorama
from datetime import datetime
import os
import random
import atexit

class logger:

    def __init__(self, log_folder: str, enable_file_logging: bool):
        self.folder = log_folder
        self.file_logging = enable_file_logging
        self.levels = {
            "info": "INFO",
            "warn": colorama.Fore.YELLOW + "WARNING" + colorama.Fore.RESET,
            "error": colorama.Fore.RED + "ERROR" + colorama.Fore.RESET,
            "exception": colorama.Fore.RED + "EXCEPTION" + colorama.Fore.RESET,
            "critical": colorama.Back.RED + "CRITICAL" + colorama.Back.RESET
        }
        self.file = f"log_{random.randint(100, 9999)}"

    def info(self, text: str):
        msg = f"[{datetime.now().date()}-{datetime.now().hour}:{datetime.now().minute} | {self.levels['info']}] {text}"
        print(msg)
        if self.file_logging:
            with open(os.path.join(self.folder) + self.file, "w") as w:
                w.write(msg)
    def warn(self, text: str):
        msg = f"[{datetime.now().date()}-{datetime.now().hour}:{datetime.now().minute} | {self.levels['warn']}] {text}"
        print(msg)
        if self.file_logging:
            with open(os.path.join(self.folder) + self.file, "w") as w:
                w.write(msg)
    def error(self, text: str):
        msg = f"[{datetime.now().date()}-{datetime.now().hour}:{datetime.now().minute} | {self.levels['error']}] {text}"
        print(msg)
        if self.file_logging:
            with open(os.path.join(self.folder) + self.file, "w") as w:
                w.write(msg)
    def exception(self, text: str):
        msg = f"[{datetime.now().date()}-{datetime.now().hour}:{datetime.now().minute} | {self.levels['exception']}] {text}"
        print(msg)
        if self.file_logging:
            with open(os.path.join(self.folder) + self.file, "w") as w:
                w.write(msg)
    def critical(self, text: str):
        msg = f"[{datetime.now().date()}-{datetime.now().hour}:{datetime.now().minute} | {self.levels['critical']}] {text}"
        print(msg)
        if self.file_logging:
            with open(os.path.join(self.folder) + self.file, "w") as w:
                w.write(msg)

if __name__ == "__main__":
    log = logger("", False)
    log.info("info")
    log.warn("warn")
    log.error("error")
    log.exception("exception")
    log.critical("critical")