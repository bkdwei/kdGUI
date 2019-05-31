'''
Created on 2019年5月25日

@author: bkd
'''
from tkinter import *
from kdGUI import Label 

root = Tk()
l = Label("bkd", root)
l.setText("hello")
l.setPadding(20)
l.setUnderline(1)
l.setEnable(True)
l.setAlignMent("left")
print(l.text(), l["justify"])
# l.clear()
l.pack()

root.mainloop()
