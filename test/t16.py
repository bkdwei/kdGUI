'''
Created on 2019年6月2日

@author: bkd
'''
from tkinter import PushButton
import tkinter

root = tkinter.Tk()
menu = tkinter.Menu(root, tearoff=0)
btn = PushButton(root, text="yes")
btn.pack()
btn_no = PushButton(root, text="no")
btn_no.pack()
menu.add_command(label="Copy")
menu.add_command(label="Paste")
menu.add_separator()
menu.add_command(label="Cut")


def popupmenu(event):
    menu.post(event.x_root, event.y_root)


btn.bind("<PushButton-3>", popupmenu)
root.mainloop()
