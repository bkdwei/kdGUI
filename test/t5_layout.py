'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import VERTICAL
from kdGUI import PushButton, RadioButton, RadioButtonGroup, Window, HorizotalLayout, Label, GridLayout


def aa():
    print("in aa")


win = Window("测试一")
win.setLayout(VERTICAL)

# b = PushButton("bkd")
# b.click(aa)
# win.addWidget(b)
# win.addWidget(PushButton("bkd1"))
# win.addWidget(PushButton("bkd2"))
# win.addWidget(PushButton("bkd3"))
# win.addWidget(PushButton("bkd4"))
# lb = Label("lbkd5")
# win.addWidget(lb)

hLayout = HorizotalLayout("aab", win)
print(win["width"])
win.addWidget(hLayout)
hLayout.addWidget(Label("bkd6", hLayout))
hLayout.addWidget(PushButton("bkd7", hLayout))
# Label(hLayout, text="o2").grid(row=2, column=0)
# Label(hLayout, text="o3").grid(row=3, column=0)
# hLayout.addWidget(Label("lbkd1"))

hLayout1 = HorizotalLayout("abc", win)
win.addWidget(hLayout1)
hLayout1.addWidget(PushButton("bkd8", hLayout1))
# hLayout1.addWidget(PushButton("bkd9"))
c = hLayout.winfo_children()
for a in c:
    print("df" + a["text"])                  
win.run()

