'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import VERTICAL
from kdGUI import Button, RadioButton, RadioButtonGroup, Window, HorizotalLayout, Label, GridLayout


def aa():
    print("in aa")


win = Window("测试一")
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
print(win["width"])
win.addWidget(hLayout)
hLayout.addWidget(Label("bkd6", hLayout))
hLayout.addWidget(Button("bkd7", hLayout))
# Label(hLayout, text="o2").grid(row=2, column=0)
# Label(hLayout, text="o3").grid(row=3, column=0)
# hLayout.addWidget(Label("lbkd1"))

hLayout1 = HorizotalLayout("abc", win)
win.addWidget(hLayout1)
hLayout1.addWidget(Button("bkd8", hLayout1))
# hLayout1.addWidget(Button("bkd9"))
                  
win.run()

