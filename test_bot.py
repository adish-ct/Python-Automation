# Import modules
import pyautogui as gui
import time

# Sleep python file for 5 Seconds
time.sleep(5)

# Open file
text = open('test_text.txt')

for line in text:
    # Type write the line
    gui.typewrite(line)
    # If you want you can hold python file to execute.