'''
Created on 2019年6月2日

@author: bkd
'''
from tkinter import *


class DragManager():

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        print("in on start", event.widget["text"])
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
#         print("in on on_drag", event.widget["text"])
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)
        print(x, y, target["text"], event.widget["text"], dir(event))
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            print("in error")
            pass


root = Tk()
label = Label(root, text="ad")
label.pack()
dnd = DragManager()
dnd.add_dragable(label)

label = Label(root, text="adc")
label.pack()
dnd1 = DragManager()
dnd1.add_dragable(label)

root.mainloop()
