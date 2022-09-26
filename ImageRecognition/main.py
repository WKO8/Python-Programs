import pyautogui
import win32api, win32con
from time import sleep

while 1:
    if pyautogui.locateOnScreen('stickerman.png', confidence=0.8) != None:
        print("I can see it")
        sleep(0.5)
        pyautogui.click()
    else:
        print("I can't to see it")
        sleep(0.5)