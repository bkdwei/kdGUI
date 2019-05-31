'''
Created on 2019年5月25日

@author: bkd
'''
from tkinter import *      

root = Tk()
l = Label(root, text="Hello, Tkinter!")
l.pack()
l.config(background='yellow')
l.config(text="bkd")

root.mainloop()
