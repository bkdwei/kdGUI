'''
Created on 2019年5月31日

@author: bkd
'''
from tkinter import * 
win = Tk()
Button(win, text="t1").grid(column=0, row=0)
Button(win, text="t2").grid(column=1, row=0)
Button(win, text="t3").grid(column=2, row=0)
Button(win, text="t4").grid(column=0, row=1)
Button(win, text="t5").grid(column=1, row=1, columnspan=2)
win.mainloop()
