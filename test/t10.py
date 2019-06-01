'''
Created on 2019年6月1日

@author: bkd
'''
import tkinter as tk
import tkinter.ttk as ttk


class AppFrame(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        entry = ttk.Entry(self)
        entry.grid(row=0, column=1, sticky='nsew')
        label = ttk.Label(self, text='Name:')
        label.grid(row=0, column=0, sticky='nsew')


root = tk.Tk()
root.title('Testlication')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame = AppFrame(root, borderwidth=15, relief='sunken')
frame.grid(row=0, column=0, sticky='nsew')
root.mainloop()
