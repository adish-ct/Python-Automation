# Import Relevant modules
import pyautogui as gui
import time

time.sleep(3)

# FAIL-SAFE : Do not disable this.
gui.FAILSAFE = True

# Open the file.
text = open('file_safe_text.txt')

# Write each line from the text
for line in text:
    gui.write(line)
    time.sleep(1)

gui.press('enter')