import pyautogui
import pytesseract
from pynput import mouse
from pynput.keyboard import Controller, Key, Listener
import pyscreenshot
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

x = 0
y = 0
button = 0
pressed = 0 

def on_click(x,y, button, pressed):
    if pressed:
        on_click.px = x
        on_click.py = y
    else:
        on_click.rx = x
        on_click.ry = y
    if not pressed:
        return False
on_click(x, y, button, pressed)  

with mouse.Listener(
                on_click = on_click) as listener:
    listener.join()

img = pyscreenshot.grab(bbox=(on_click.px, on_click.py, on_click.rx, on_click.ry))

txt = str(pytesseract.image_to_string(img, lang = "eng")).replace('|', 'I')
txt = ' '.join(txt.splitlines())
print(txt)

keyboard = Controller()

def on_press(key):
    if key == Key.num_lock:
        for i in txt:
            keyboard.press(i)
            keyboard.release(i)
            time.sleep(0.05)

with Listener(on_press = on_press) as listener:
    listener.join()