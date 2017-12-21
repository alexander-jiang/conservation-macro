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
time.sleep(10) # wait for the app to load

# tab-cycle to the hardware settings menu
for i in range(12):
    time.sleep(0.2)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# tab-cycle to the power menu
for i in range(9):
    time.sleep(0.2)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# tab-cycle to the conservation mode option
for i in range(5):
    time.sleep(0.2)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
time.sleep(0.5)
keyboard.press(Key.space)
keyboard.release(Key.space)
