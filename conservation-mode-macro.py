# from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# show desktop (don't want anything to interfere with the input)
keyboard.press(Key.cmd)
keyboard.press('d')
keyboard.release('d')
keyboard.release(Key.cmd)
time.sleep(0.2)

keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(0.5)
keyboard.type('companion')
time.sleep(1) # wait a longer for the search result to show up
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5) # app takes a while to load sometimes
for i in range(12):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.5)

for i in range(9):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)
for i in range(5):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.2)
keyboard.press(Key.space)
keyboard.release(Key.space)
