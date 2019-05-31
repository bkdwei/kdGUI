'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import *
from kdGUI import Button, RadioButton, RadioButtonGroup, Window, HorizotalLayout


def aa():
    print("in aa")


win = Window()
win.setLayout(Window.GRID)
b = Button("bkd")
b.click(aa)
win.addWidget(b, 0, 0)
win.addWidget(Button("bkd1"), 0, 1)
win.addWidget(Button("bkd2"), 1, 0)
win.addWidget(Button("bkd3"), 1, 1)
win.addWidget(Button("bkd3"), 1, 2)

win.run()

