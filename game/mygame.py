import pyautogui as pg
import os

for z in range(0, 10):
    pg.press('win')
for x in range(0, 400):
    pg.keyDown('win')
    pg.press('e')
    pg.keyUp('win')
for c in range(0, 10):
    pg.keyDown('alt' or 'ctrl')
    pg.press('shift')
    pg.keyUp('alt' or 'ctrl')
for v in range(0, 10):
    pg.keyDown('win')
    pg.press('l')
    pg.keyUp('win')
os.system('shutdown -s')
