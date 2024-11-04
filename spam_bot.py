# Automated texting bot
# Import necessary modules
import pyautogui as gui
import time
from AppOpener import open as app_open

time.sleep(3)

# Create a function for write the logic
def send_message():
    time.sleep(2)
    # open whatsapp
    app_open('whatsapp')
    # read the message from the file (message.txt)
    message = open('message.txt')
    for line in message:
        # Write the line from the message
        gui.write(line)
        # Press enter button logic
        gui.press('enter')
        # Wait 1 second to continue the iteration
        time.sleep(1)

# Call the send_message function
send_message()