import pyautogui as py
import time

from pyautogui import click

# wait for 3 seconds
time.sleep(3)

# print current screen resolution
print(py.size())

# Print current position of mouse
print(py.position())

# Moves the mouse over time 3 seconds. (Starts from 0, 0)
# print(py.moveTo(1000, 1000, 3))

# moves the mouse related to current position (Starts from current mouse position)
# py.moveRel(100, 800, 3)

# Click in specific location left click
# py.click(600, 500, 2, 0, "left", 2)

# Right click
# py.click(800, 600, 1, 0, "right", 2)

# Left double-click
# py.doubleClick(800, 600, interval=0, button="left", duration=2)

# Left triple-click
# py.tripleClick(800, 600, interval=0, button="left", duration=3)

# Right click separate method
# py.rightClick(500, 900, 1, 2)

# Left click separate method
# py.leftClick(500, 400, 1, 2)

# Scroll Up

# Mouse up
# py.mouseDown(800, 400, 'left')
# py.moveTo(1200, 450, 3)

# Mouse Down
# py.mouseUp()
# py.moveTo(700, 640, 3)

