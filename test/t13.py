'''
Created on 2019年6月2日

@author: bkd
'''

from tkinter import Label

from TkinterDnD2 import *


def drop(event):
    print("in drop", event.data)


def drop_enter(event):
    event.widget.focus_force()
    print('Entering widget: %s' % event.widget)
    # print_event_info(event)
    return event.action


def drag_init_text(event):
    data = 'adf'
    print('Dragging :\n', data)
    # if there is only one possible alternative for action and DnD type
    # we can also use strings here
    return (COPY, DND_TEXT, data)


root = TkinterDnD.Tk()
root.withdraw()
root.title('TkinterDnD demo')
lb_verticalLayout = Label(root, text="abc")
lb_verticalLayout.dnd_bind('<<Drop>>', drop)
lb_verticalLayout.dnd_bind('<<DropEnter>>', drop_enter)
lb_verticalLayout.dnd_bind('<<DragInitCmd>>', drag_init_text)
lb_verticalLayout.drag_source_register(1, DND_TEXT)
lb_verticalLayout.pack()
root.update_idletasks()
root.deiconify()
root.mainloop()
