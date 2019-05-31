'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import VERTICAL, Label
from kdGUI import Button, RadioButton, RadioButtonGroup, Window, HorizotalLayout


def aa():
    print("in aa")


win = Window()
win.setLayout(VERTICAL)
# b = Button("bkd")
# b.click(aa)
# win.addWidget(b)
# win.addWidget(Button("bkd1"))
# win.addWidget(Button("bkd2"))
# win.addWidget(Button("bkd3"))
# win.addWidget(Button("bkd4"))
# lb = Label("lbkd5")
# win.addWidget(lb)

hLayout = HorizotalLayout("aab", win)
win.addWidget(hLayout)
hLayout.addWidget(Button("bkd6"))
hLayout.addWidget(Button("bkd7"))
# Label(hLayout, text="o2").grid(row=2, column=0)
# Label(hLayout, text="o3").grid(row=3, column=0)
# hLayout.addWidget(Label("lbkd1"))

hLayout1 = HorizotalLayout("abc", win)
win.addWidget(hLayout1)
# hLayout1.addWidget(Button("bkd8"))
# hLayout1.addWidget(Button("bkd9"))
                  
win.run()

