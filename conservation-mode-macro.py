from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

kbdController = Controller()

# show desktop (don't want anything to interfere with the input)
# kbdController.press(Key.cmd)
# kbdController.press('d')
# kbdController.release('d')
# kbdController.release(Key.cmd)
# time.sleep(0.1)

# open start menu (to search for the app)
kbdController.press(Key.cmd)
kbdController.release(Key.cmd)
time.sleep(0.2)
kbdController.type('companion')
time.sleep(0.5) # wait a longer for the search result to show up
kbdController.press(Key.enter)
kbdController.release(Key.enter)


class ReadyException(Exception): pass

def ready_on_enter(key):
    if key == Key.enter:
        raise ReadyException(key)

# press enter once the app has loaded
with keyboard.Listener(
        on_press=ready_on_enter) as listener:
    try:
        print("when the window finishes loading, press enter")
        listener.join()
    except ReadyException as e:
        print("enter was pressed")
        listener.stop()

# tab-cycle to the hardware settings menu
for i in range(12):
    kbdController.press(Key.tab)
    kbdController.release(Key.tab)
    time.sleep(0.1)
kbdController.press(Key.enter)
kbdController.release(Key.enter)
time.sleep(1)

# tab-cycle to the power menu
for i in range(9):
    kbdController.press(Key.tab)
    kbdController.release(Key.tab)
    time.sleep(0.1)
kbdController.press(Key.enter)
kbdController.release(Key.enter)
time.sleep(1)

# tab-cycle to the conservation mode option
for i in range(6):
    kbdController.press(Key.tab)
    kbdController.release(Key.tab)
    time.sleep(0.1)

# check that we actually toggled the conservation mode setting
config_file = open("setting_filename.conf", 'r')
setting_filename = config_file.readline().strip()

f_before = open(setting_filename, 'r')
lines_before = f_before.readlines()
f_before.close()

charge_mode = ""
setting_str = "<Setting key=\"BatteryChargeMode\">"
for line in lines_before:
    start_index = line.find(setting_str)
    end_index = line.find("</Setting>")
    if start_index != -1:
        charge_mode = line[start_index + len(setting_str):end_index]
        print("battery charge mode setting: %s" % charge_mode)

kbdController.press(Key.space)
kbdController.release(Key.space)
time.sleep(0.5)

f_after = open(setting_filename, 'r')
lines_after = f_after.readlines()
f_after.close()
for line in lines_after:
    start_index = line.find(setting_str)
    end_index = line.find("</Setting>")
    if start_index != -1:
        charge_mode2 = line[start_index + len(setting_str):end_index]
        print("detected battery charge mode: %s" % charge_mode2)
        if charge_mode2 == charge_mode:
            # didn't change the setting; undo the change
            print("failed to update the conservation mode setting. undoing change...")
            kbdController.press(Key.space)
            kbdController.release(Key.space)

# clean up: close the window
with kbdController.pressed(Key.alt):
    kbdController.press(Key.f4)
    kbdController.release(Key.f4)
