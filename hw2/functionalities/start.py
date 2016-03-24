__author__ = 'Suota'

from functionalities import gui , histogram
from tkinter import *


def setup_choice_window ():

    # setting up first window with choice histogram / editor

    root = Tk()
    frame = Frame(root)
    frame.pack()

    rightbutton = Button(frame, text="Histogram", command = histogram.set_hist , fg="red")
    rightbutton.pack( side = RIGHT)

    leftbutton = Button(frame, text="Editor", command = gui.setGUI , fg="red")
    leftbutton.pack( side = LEFT)

    root.mainloop()