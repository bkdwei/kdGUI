'''
Created on 2019年5月25日

@author: bkd
'''
from tkinter import ttk, StringVar, Widget
import tkinter
from tkinter.constants import VERTICAL, HORIZONTAL, N, E, S, W


class Label(tkinter.Label):
    """
    标签
    """
    
    def __init__(self, text=None, parent=None):
        super().__init__(parent, text=text)
        
    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text

    def setUnderline(self, underline):
        self["underline"] = underline

    def setPadding(self, padding):
        self["width"] = padding

    def setEnable(self, boolean):
        if boolean:
            self["state"] = "active"
        else :
            self["state"] = "disabled"
    
    def setAlignMent(self, alignMent):
        self["justify"] = alignMent

    def clear(self):
        self["text"] = ""


class Button(ttk.Button):
    """
    按钮
    """

    def __init__(self, text=None, parent=None):
        super().__init__(parent, text=text)
        self.cnf = {"text":text}

    def click(self, function):
        self["command"] = function

    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text


class RadioButton(tkinter.Radiobutton):
    """
    单选按钮
    """

    def __init__(self, text=None, parent=None, RadioButtonGroup=None):
        super().__init__(parent, text=text)
        self["value"] = text
        if RadioButtonGroup :
            self.group = RadioButtonGroup
            self.setGroup(RadioButtonGroup)
            
        self.data = None

    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text

    def isChecked(self):
        return self.group.get() == self["value"]

    def click(self, function):
        self["command"] = function

    def setGroup(self, group):
        # 用于判断是否被选中
        self.group = group
        # 用于同步gropu的变化
        self["variable"] = group

    def value(self):
        return self.data
    
    def setValue(self, data):
        self.data = data

    def setChecked(self, boolean):
        if boolean:
            self.group.set(self["value"])
        else :
            self.group.set(None)


class RadioButtonGroup(StringVar):

    def __init__(self):
        super().__init__()


class Window(tkinter.Tk):

    GRID = "grid"

    def __init__(self):
        super().__init__()  
        self.layout = VERTICAL
        self.rowIndex = 0 
        self.columnIndex = 0
        
    def run(self):
        self.mainloop()

    def setLayout(self, layout):
        self.layout = layout    

    def addWidget(self, widget, row=None, column=None):
#         widget.master = self
#         widget.tk = self.tk
        Widget.__init__(widget, self, widget.widgetName, widget.cnf, {}, ())
#         widget._setup(self, None)
        if self.layout == VERTICAL:
            print(self.rowIndex, self.columnIndex, widget.widgetName)
            widget.grid(row=self.rowIndex, column=self.columnIndex)
            self.rowIndex += 1
        elif self.layout == HORIZONTAL :
            widget.grid(row=self.rowIndex, column=self.columnIndex)
            self.columnIndex += 1
        elif self.layout == self.GRID :
            if row == None:
                raise RuntimeError(" row can not be None")
            if column == None :
                raise RuntimeError("column can not be None")
            widget.grid(row=row, column=column)


class HorizotalLayout(tkinter.LabelFrame):

    def __init__(self, text=None, parent=None):
        super().__init__(text=text, bd=10, master=parent)  
#         self.grid(column=0, row=0, sticky=(N, W, E, S))
#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(0, weight=1)
        self.cnf = {"text":text, "bd":10, "height":300, "width":300}
        self.rowIndex = 0
#         self["bg"] = "blue"
#         self["bd"] = 5
        self["height"] = 300
        self["width"] = 300
    
    def setRowIndex(self, index):
        self.rowIndex = index
        
    def addWidget(self, widget):
#         widget.master = self
#         widget.tk = self
#         name = None
#         if not name:
#             name = repr(id(self))
#         self._name = name
#         master = self
#         if master._w == '.':
#             widget._w = '.' + name
#         else:
#             widget._w = master._w + '.' + name
#         widget.children = {}
#         if widget._name in widget.master.children:
#             widget.master.children[widget._name].destroy()
#         widget.master.children[widget._name] = self
        Widget.__init__(widget, self, widget.widgetName, widget.cnf, {}, ())
        
#         widget.pack()
        widget.grid(row=self.rowIndex, column=0)
        print(self.rowIndex, widget.widgetName)
        self.rowIndex += 1
