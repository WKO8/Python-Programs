import pyperclip
from pynput.keyboard import Key
from pynput.mouse import Button


import time

name = "Your text to copy and paste"
pyperclip.copy(name)

def send():
    from pynput.keyboard import Controller
    keyb = Controller()
    keyb.press(Key.alt)
    keyb.press(Key.tab)
    keyb.release(Key.tab)

    from pynput.mouse import Controller
    mouse = Controller()
    mouse.position = (952, 552)
    mouse.click(Button.left)

    keyb.release(Key.alt)
    
    mouse.position = (700, 945)
    mouse.click(Button.left)
    pyperclip.paste()
    
    keyb.press(Key.enter)
    keyb.release(Key.enter)
