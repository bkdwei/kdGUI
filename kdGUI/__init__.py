'''
Created on 2019年5月25日

@author: bkd
'''
from tkinter import ttk, StringVar, Widget
import tkinter
from tkinter.constants import VERTICAL, HORIZONTAL, N, E, S, W

_default_root = None


class Window(tkinter.Tk):

    GRID = "grid"

    def __init__(self, title=None):
        if title :
            super().__init__(className=title)
        else:
            super().__init__()
        self.layout = VERTICAL
        self.rowIndex = 0 
        self.columnIndex = 0
            
        global _default_root
        _default_root = self
        
    def run(self):
        self.mainloop()

    def setLayout(self, layout):
        self.layout = layout    

    def addWidget(self, widget, row=None, column=None):
        if self.layout == VERTICAL:
            print(self.rowIndex, self.columnIndex, widget.widgetName)
            widget.grid(row=self.rowIndex, column=self.columnIndex, sticky="w" + "e")
            self.rowIndex += 1
        elif self.layout == HORIZONTAL :
            widget.grid(row=self.rowIndex, column=self.columnIndex)
            self.columnIndex += 1
        elif self.layout == self.GRID :
            if row == None:
                raise RuntimeError("row can not be None")
            if column == None :
                raise RuntimeError("column can not be None")
            widget.grid(row=row, column=column)


class HorizotalLayout(tkinter.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent :
            global _default_root
            parent = _default_root
        super().__init__(text=text, bd=10, master=parent)  
#         self.grid(column=0, row=0, sticky=(N, W, E, S))
#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(0, weight=1)
#         self.cnf = {"text":text, "bd":10, "height":300, "width":300}
        self.rowIndex = 0
#         self["bg"] = "blue"
#         self["bd"] = 5
#         self["height"] = 300
#         self["width"] = 300
    
    def setRowIndex(self, index):
        self.rowIndex = index
        
    def addWidget(self, widget):
        widget.grid(row=self.rowIndex, column=0)
        print(self.rowIndex, widget.widgetName)
        self.rowIndex += 1


class VerticalLayout(tkinter.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent :
            global _default_root
            parent = _default_root
        super().__init__(text=text, bd=10, master=parent)  
#         self.grid(column=0, row=0, sticky=(N, W, E, S))
#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(0, weight=1)
#         self.cnf = {"text":text, "bd":10, "height":300, "width":300}
        self.columnIndex = 0
#         self["bg"] = "blue"
#         self["bd"] = 5
#         self["height"] = 300
#         self["width"] = 300
    
    def setHeight(self, height):
        self["height"] = height
        
    def addWidget(self, widget):
        widget.grid(row=0, column=self.columnIndex)
        self.columnIndex += 1


class GridLayout(tkinter.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent :
            global _default_root
            parent = _default_root
        super().__init__(text=text, bd=10, master=parent)  

    def setRowIndex(self, index):
        self.rowIndex = index
        
    def addWidget(self, widget, row, column, rowspan=1, columnspan=1):
        widget.grid(row=row, column=column , rowspan=rowspan, columnspan=columnspan, sticky="w" + "e")

                
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
    
    def setHeight(self, height):
        self["height"] = height        


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


class LineEdit(ttk.Entry):

    def __init__(self, defaultValue=None, parent=None):
        super().__init__(master=parent)
        self.contents = StringVar()
        self["textvariable"] = self.contents
        if defaultValue:
            self.contents.set(defaultValue)

    def text(self):
        return self.contents.get()

    def setText(self, text):
        self.contents.set(text)


class CheckBox(ttk.Checkbutton):

    def __init__(self, text=None, parent=None):
        super().__init__(master=parent, text=text)
