'''
Created on 2019年5月25日

@author: bkd
'''
from tkinter import *      


def get_variable_name(x):
    for k, v in locals().items():
        if v is x:
            return k


def print_var(x):
    print(get_variable_name(x), '=', x)

    
root = Tk()
l = Label(root, text="Hello, Tkinter!")
l.pack()
l.config(background='yellow')
l.config(text="bkd")
a = "09"
b = int(a)
print(b)
print_var(l)
print(locals())
root.mainloop()

