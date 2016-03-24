__author__ = 'Suota'

from tkinter import *
from HW3 import download ,astro

mars = False
jupiter = False
moon = False
saturn = False
fb = False
tw = False
ms = False
goog = False


def setGUI():

    global top
    top = Tk()

    t = Text(top, bg = 'green' , font= 20 , height= 2 , width = 28)
    t.insert(INSERT,"  Choose planet and time period  ")
    t.insert(INSERT, " Default time = 1 year")
    t.pack(side=TOP)

    frame1 = Frame(top)
    frame1.pack(side=LEFT)

    frame3 = Frame(top)
    frame3.pack(side=BOTTOM)

    CheckVar = IntVar()

# group of radiobuttons to choose one planet

    C1 = Radiobutton(frame1, text = "MARS",command = mars_on, value=0,variable = CheckVar)
    C2 = Radiobutton(frame1, text = "Jupiter",command = jupiter_on, value=1,variable = CheckVar)
    C3 = Radiobutton(frame1, text = "Saturn",command = saturn_on,value=2, variable = CheckVar)
    C4 = Radiobutton(frame1, text = "Moon", command = moon_on,value =3, variable = CheckVar)

    C1.pack(anchor = W)
    C2.pack(anchor = W)
    C3.pack(anchor = W)
    C4.pack(anchor = W)


    CheckVar3 = IntVar()

# radiobuttons to choose time of last week or last month of data to compare

    T1 = Radiobutton(frame3, text = "last month",command = download.month, value="8",variable = CheckVar3)
    T2 = Radiobutton(frame3, text = "last week",command = download.week, value="9",variable = CheckVar3)

    T1.pack(anchor = W)
    T2.pack(anchor = W)

# button to plot data and close current window

    startbutton = Button(frame3, text = "Draw" , command = draw )
    startbutton.pack(side = BOTTOM)

    top.protocol("WM_DELETE_WINDOW", draw)
    top.mainloop()

def draw():

# closing current window, plotting one planet data and opening new window to choose company

    top.destroy()

    global top1
    top1 = Tk()
    t1 = Text(top1, bg = 'green' , font= 20 , height= 1 , width = 34)
    t1.insert(INSERT,"  Now choose company to compare ")
    t1.pack(side=TOP)

    frame2 = Frame(top1)
    frame2.pack(side=RIGHT)

    CheckVar2 = IntVar()

# radiobuttons to choose a company to compare

    P1 = Radiobutton(frame2, text = "Facebook",command =on_fb, value=4,variable = CheckVar2)
    P2 = Radiobutton(frame2, text = "Google",command = on_goog, value=5,variable = CheckVar2)
    P3 = Radiobutton(frame2, text = "Microsoft",command = on_ms,value=6, variable = CheckVar2)
    P4 = Radiobutton(frame2, text = "Twitter", command = on_tw,value =7, variable = CheckVar2)

    P1.pack(anchor = W)
    P2.pack(anchor = W)
    P3.pack(anchor = W)
    P4.pack(anchor = W)

    button = Button(top1, text= "Draw" , command = draw2 )
    button.pack(side=BOTTOM)

# plotting planet's distance from Earth

    if mars:
        astro.set_mars()
    if jupiter:
        astro.set_jupiter()
    if moon:
        astro.set_moon()
    if saturn:
        astro.set_saturn()

    top1.mainloop()


def draw2():

# closing window with company radiobuttons
# plotting selected company
    top1.destroy()
    if fb:
        download.set_fb()
    if ms:
        download.set_ms()
    if goog:
        download.set_goog()
    if tw:
        download.set_tw()


def mars_on():
    global mars
    mars = True
def saturn_on():
    global saturn
    saturn = True
def moon_on():
    global moon
    moon = True
def jupiter_on():
    global jupiter
    jupiter= True
def on_fb():
    global fb
    fb = True
def on_ms():
    global ms
    ms = True
def on_tw():
    global tw
    tw = True
def on_goog():
    global goog
    goog = True
