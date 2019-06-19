'''
Created on 2019年6月19日

@author: bkd
'''
import tkinter as tk


def populate(frame):
    '''Put in some fake data'''
    for row in range(100):
        tk.Label(frame, text="%s" % row, width=3, borderwidth="1",
                 relief="solid").grid(row=row, column=0)
        t = "this is the second column for row %s" % row
        tk.Label(frame, text=t).grid(row=row, column=1)


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="blue")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview, width=32)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

frame.pack(fill=tk.Y, expand=True)
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
# frame.columnconfigure(1, weight=1)
populate(frame)

root.mainloop()
