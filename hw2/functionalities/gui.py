

from tkinter import *
import tkinter
from functionalities import editor


def setGUI():

    # creating new window with frame inside

    root = Tk()
    frame = Frame(root)
    frame.pack()

    tkim = tkinter.PhotoImage(file=sys.argv[1])

    w = Label(frame , image = tkim)
    w.pack(side= TOP)

    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )

# creating button for black and white image

    bwbutton = Button(bottomframe, text="Black & White", command = editor.b_and_white , fg="red")
    bwbutton.pack( side = RIGHT)

# creating button for dividing image

    partbutton = Button(bottomframe, text="Divide and join", command = editor.part , fg="blue")
    partbutton.pack( side = RIGHT )

# creating button for softening edges

    edgesbutton = Button(bottomframe, text="Soften edges", command = editor.edges , fg="black")
    edgesbutton.pack( side = RIGHT)

# creating 3 -options radiobutton
    var = IntVar()
    r1 = Radiobutton(frame, text= "Decrease RGB values", variable=var, value=1,
                  command=editor.darken )
    r1.pack( anchor = W )

    r2 = Radiobutton(frame, text="Increase RGB values", variable=var, value=2,
                  command=editor.whiten)
    r2.pack( anchor = W )

    r3 = Radiobutton(frame, text="Weaken colors", variable=var, value=3,
                     command= editor.color)
    r3.pack( anchor = W)


# keeping GUI displayed

    root.mainloop()
