'''
Created on 2019年6月11日

@author: bkd
'''
import tkinter as tk

window = tk.Tk()
window.title("我的窗口")
window.geometry('600x400')

var1 = tk.StringVar()
label = tk.Label(window, bg='yellow',
                 width=30, heigh=2, text="empty")
label.pack()


def select(v):
    label.config(text='你选择的是：' + v)


# scale 尺子属性注释：
# orient ＝ tk.HORIZONTAL 水平还是竖直
# legnth 是长度
# showvalue 0:不显示，1:显示
# tickinterval 标注分成几段
# resolution 最小单位或者说保留到几位
# command 方法需要由一个参数接收选择的当前刻度
sc = tk.Scale(window, label="拉动", from_=0, to=12, orient=tk.HORIZONTAL,
              length=500, showvalue=1, tickinterval=3, resolution=0.01, command=select)
sc.pack()
sc.set(5)
window.mainloop()
