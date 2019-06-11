'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import *
from kdGUI import PushButton, RadioButton, RadioButtonGroup, Window, HorizotalLayout


def aa():
    print("in aa")


win = Window()
win.setLayout(Window.GRID)
b = PushButton("bkd")
b.click(aa)
win.addWidget(b, 0, 0)
win.addWidget(PushButton("bkd1"), 0, 1)
win.addWidget(PushButton("bkd2"), 1, 0)
win.addWidget(PushButton("bkd3"), 1, 1)
win.addWidget(PushButton("bkd3"), 1, 2)

win.run()

