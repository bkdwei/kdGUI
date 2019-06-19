'''
Created on 2019年6月19日

@author: bkd
'''
from tkinter import *


def data():
    for i in range(50):
       Label(frame, text=i).grid(row=i, column=0)
       Label(frame, text="my text" + str(i)).grid(row=i, column=1)
       Label(frame, text="..........").grid(row=i, column=2)


def myfunction(event):
#     canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)
        canvas.configure(scrollregion=canvas.bbox("all"))
#     pass


root = Tk()
# sizex = 800
# sizey = 600
# posx = 100
# posy = 100
# root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

# myframe = Frame(root, relief=GROOVE, width=50, height=100, bd=1)
myframe = Frame(root, bd=5, background="blue")
# myframe.place(x=10, y=10)
myframe.pack()

# 外框架 [画布[内框架]，滚动条]
# 1.画布
canvas = Canvas(myframe)

# 2.画布上的内框架
frame = Frame(canvas, bd=5, background="red")
# canvas.create_window((0, 0), window=frame, anchor='nw')
canvas.create_window((0, 0), window=frame)
# 3.外框架上的滚动条
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview, bd=5, background="yellow", width=25)

# 配置外框架内的组件的位置
canvas.pack(side="left", fill=BOTH, expand=True)
myscrollbar.pack(side="right", fill="y")

# 配置动作
canvas.configure(yscrollcommand=myscrollbar.set)
frame.bind("<Configure>", myfunction)
data()
root.mainloop()
