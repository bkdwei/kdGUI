'''
Created on 2019年5月26日

@author: bkd
'''
''' tk_LabelFrame_grid_layout1.py
grid layout of frames
'''
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
root = tk.Tk()
root.geometry("320x400")
frame1 = tk.LabelFrame(root, text="frame1", width=300, height=130, bd=5)
frame2 = tk.LabelFrame(frame1, text="frame2", width=150, height=130, bd=5)
frame3 = tk.LabelFrame(root, text="frame3", width=140, height=100, bd=5)
frame4 = tk.LabelFrame(root, text="frame4", width=300, height=130, bd=5)
frame1.grid(row=0, column=0, columnspan=2, padx=8)
frame2.grid(row=2, column=0, padx=8)
frame3.grid(row=2, column=0, sticky='nw')
frame4.grid(row=3, column=0, columnspan=2)
ll = tk.Label(frame1, text="a").grid(row=0, column=0)
tk.Label(frame1, text="b").grid(row=1, column=0)

lll = tk.Label(frame2, text="a1").grid(row=0, column=0)
tk.Label(frame2, text="b2").grid(row=1, column=0)

print(dir(ll))
root.mainloop()
