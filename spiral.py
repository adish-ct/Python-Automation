import pyautogui as gui
import time

time.sleep(3)

distance = 300
gui.moveTo(700, 450)


while distance > 20:
    gui.dragRel(distance, 0, 1, button='left')
    distance -= 20
    gui.dragRel(0, distance, 1, button='left')
    gui.dragRel(-distance, 0, 1, button='left')
    distance -= 20
    gui.dragRel(0, -distance, 1, button='left')
