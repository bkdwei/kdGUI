'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import *
from kdGUI import Button, RadioButton, RadioButtonGroup


def aa():
    print("in aa")


def ab():
    print(rb3.isChecked())


root = Tk()
b = Button("bkd", root)
b.click(aa)
b.pack()

v = RadioButtonGroup()

rb = RadioButton("rb", root)
rb3 = RadioButton("rb2", root)

rb.setGroup(v)
rb3.setGroup(v)
# v.set("rb")
rb3.setChecked(False)
# rb3.setValue("rb2")
print(rb.value(), rb3.value(), v.get())
rb3.click(ab)
rb.pack()
rb3.pack()

root.mainloop()
