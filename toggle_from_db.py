from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

keyboard.type('cd C:\Users\dashu\AppData\Local\Packages\E046963F.LenovoCompanion_k1h2ywk1493x8\LocalState')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.type('sqlite3')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.type('.open KeywordsDB.db')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
