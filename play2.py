from tkinter import *
import random
import ctypes
import threading
import time

ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ------------------------------------------------------------------------------------------------------#

# global scopes#
counter = 0
is_on = False


# ------------------------------------------------------------------------------------------------------#
# FUNCTIONS
# TODO 3: Check if user typed same text as sample.
def check(text):
    global is_on
    if not is_on:
        if not text.keycode in [16, 17, 18]:
            is_on = True
            t = threading.Thread(target=time_thread)
            t.start()

    # TODO 5: Change background color red if its false.
    if not text_label.cget('text').startswith(entry.get()):
        entry.config(fg="red")
    else:
        entry.config(fg="green")
        # TODO 4: Change background color green i"f its true.
    if entry.get() == text_label.cget('text')[:-1]:
        entry.config(fg="green")
        is_on = False


# calculate time function
def time_thread():
    while is_on:
        global counter
        time.sleep(0.1)
        counter += 0.1
        s = len(entry.get().split(" ")) / counter
        wpm = s * 60
        speed_label.config(text=f"Speed: {wpm:.2f} WPM")


def reset():
    global counter
    is_on = False
    counter = 0
    speed_label.config(text="Speed: 0.00 WPM")
    text_label.config(text=random.choice(a))
    entry.delete(0, END)


# ------------------------------------------------------------------------------------------------------#
# TODO 1: Create Text sample.

with open("Text.txt", "r") as file:
    a = file.read().split("\n")
    text = random.choice(a)
# ------------------------------------------------------------------------------------------------------#
# TODO 2: Create a GUI .

root = Tk()
root.title("Typing Speed")
root.geometry("900x400")
root.option_add("*Label.Font", "consolas 15")
root.option_add("*Button.Font", "consolas 15")

frame = Frame(root)

text_label = Label(root, text=text)
text_label.grid(column=0, row=1, padx=50, pady=50)

speed_label = Label(frame, text="Speed: 0.00 WPS", font=("Helventica", 18),pady=25)
speed_label.grid(column=0, row=3)

reset_button = Button(text="reset", command=reset)
reset_button.grid(row=3, column=0)

entry = Entry(frame,width=40)
entry.grid(column=0, row=2)
entry.bind("<KeyPress>", check)

frame.grid(column=0, row=2)

root.mainloop()
