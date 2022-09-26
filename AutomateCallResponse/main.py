from pyautogui import press, typewrite, hotkey
from pynput.keyboard import Listener, Key

import pyautogui

# Press PB (PauseBreak) to exit

try:
    name = 'Your name to type in the Google Meet chat'
    def send():
        hotkey('win', '2')
        pyautogui.click(x=1700, y=960)
        typewrite(name)
        hotkey('enter')
    
    def write_send():
        pyautogui.click(x=1700, y=960)
        typewrite(name)
        hotkey('enter')

    def leave():
        pyautogui.click(x=1795, y=1035)
        hotkey('ctrl', 'w')

    def press(key):
        if key == Key.f9:
            send()
        elif key == Key.f10:
            write_send()
        elif key == Key.f8:
            leave()
        elif key == Key.pause:
            exit()
        
    def release(key):
        print(key)

    with Listener(on_press=press, on_release=release) as listener:
        listener.join()
except:
    pass