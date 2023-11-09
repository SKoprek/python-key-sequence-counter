# from pynput import keyboard
# from tkinter import *
#
# space = 0
# throws = 0
# skull_jumps = 0
# previous = 0
# record = 0
#
#
# def on_press(key):
#     global skull_jumps
#     global throws
#     global record
#     global previous
#     if key == keyboard.Key.space:
#         throws += 1
#         if throws % 2 == 0:
#             skull_jumps = round((throws / 2))
#             label_reload()
#     if key == keyboard.KeyCode.from_char('w') or key == keyboard.Key.up:
#         if skull_jumps > 0:
#             previous = skull_jumps - 1
#         if skull_jumps > record:
#             record = skull_jumps - 1
#         throws = 0
#         skull_jumps = 0
#         label_reload()
#         print('RESET')
#     if key == keyboard.KeyCode.from_char('q'):
#         record = 0
#
#
#
# def label_reload():
#     label_0.config(text=("Throws: " + str(throws)))
#     label_0.pack()
#     label_1.config(text=("Skull jumps: " + str(skull_jumps) + " ?"))
#     label_1.pack()
#     label_2.config(text=("Previous: " + str(previous)))
#     label_2.pack()
#     label_3.config(text=("Record: " + str(record)))
#     label_3.pack()
#
#
# if __name__ == '__main__':
#     window = Tk()
#     window.call('wm', 'attributes', '.', '-topmost', '1')
#     window.title("Skull jumps counter helper")
#     label_0 = Label(window, text=("Throws: " + str(throws)))
#     label_0.pack()
#     label_1 = Label(window, text=("Skull jumps: " + str(skull_jumps)))
#     label_1.pack()
#     label_2 = Label(window, text=("Previous: " + str(previous)))
#     label_2.pack()
#     label_3 = Label(window, text=("Record: " + str(record)))
#     label_3.pack()
#     with keyboard.Listener(on_press=on_press) as lis:
#         mainloop()
#         lis.join()
#
#
#
#
#
#
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
keyboard.press(Key.z)
time.sleep(.05)
keyboard.release(Key.f12)