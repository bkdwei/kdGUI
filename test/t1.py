'''
Created on 2019年5月25日

@author: bkd
'''
from tkinter import *   
import tkinter.ttk as ttk   


def get_variable_name(x):
    for k, v in locals().items():
        if v is x:
            return k


def print_var(x):
    print(get_variable_name(x), '=', x)

    
root = Tk()
l = Label(root, text="Hello, Tkinter!")
l.grid(row=0, column=0)
# l.pack()
# l.config(background='yellow')
# l.config(text="bkd")
# a = "09"
# b = int(a)
# print(b)
# print_var(l)
# print(locals())

_separator = ttk.Separator(root, orient="horizontal")
_separator.grid(row=1, column=0, sticky="nswe")
l = Label(root, text="Hello, Tkinter!")
l.grid(row=2, column=0)
        
root.mainloop()

