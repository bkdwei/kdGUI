'''
Created on 2019年6月1日

@author: bkd
'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END, str(i * 100))
print(lb.get(3))
print(lb.size())
lb.pack()
root.mainloop()
