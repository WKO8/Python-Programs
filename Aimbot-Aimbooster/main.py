import pyautogui
import keyboard
import win32api, win32con
from time import sleep

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('c') == False:
    print("Started scrolling across the screen")
    screen = pyautogui.screenshot(region=(1252, 767, 400, 280))
    width, height = screen.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = screen.getpixel((x, y))

            if r == 255 and g == 219 and b == 195:
                # pyautogui.click(1252+x, 767+y)
                click(1252+x, 767+y)
                sleep(0.05)
                break