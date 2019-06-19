'''
Created on 2019年5月25日

@author: bkd
'''
from sys import platform
from tkinter import tix
from tkinter import ttk
from tkinter.constants import *

from ttkthemes import ThemedTk
from ttkthemes._widget import ThemedWidget

import tkinter as tk

_default_root = None


class Window(tix.Tk):

    GRID = "grid"

    def __init__(self, title=None):
        if title:
            super().__init__(className=title)
        else:
            super().__init__()
        self.layout = VERTICAL
        self.rowIndex = 0
        self.columnIndex = 0

        global _default_root
        _default_root = self
        self.statusbar = Label("状态栏", self)
        self.statusbar.setAnchor("w")
#         self.addWidget(self.statusbar, expand=YES)
#         self.statusbar.pack(
#             fill=BOTH, expand=NO, side=BOTTOM)

    def run(self):
        self.mainloop()

    def setLayout(self, layout):
        self.layout = layout

    def addWidget(self, widget, row=None, column=None, expand=NO):
        if self.layout == VERTICAL:
#             print(self.rowIndex, self.columnIndex,
#                   widget.widgetName)
#             widget.grid(row=self.rowIndex, column=self.columnIndex, sticky="w" + "e")
#             self.rowIndex += 1
            widget.pack(fill=BOTH, expand=expand)
        elif self.layout == HORIZONTAL:
            #             widget.grid(row=self.rowIndex, column=self.columnIndex)
            #             self.columnIndex += 1
            widget.pack(fill=BOTH, expand=expand, side=LEFT)
        elif self.layout == self.GRID:
            if row == None:
                raise RuntimeError("row can not be None")
            if column == None:
                raise RuntimeError("column can not be None")
            widget.grid(row=row, column=column)

    def setTitle(self, title):
        self.title(title)

    def showMaximized(self):
        #         w, h = self.maxsize()
        if platform == "win32" :
            self.state("zoomed")
            return
        else:
            w = self.winfo_screenwidth()
            h = self.winfo_screenheight()
            self.geometry("{}x{}".format(w, h))

    def showFullScreen(self):
        self.attributes("-fullscreen", True)

    def childrens(self):
        return self.winfo_children()

    def showMessage(self, msg):
        self.statusbar.setText(msg)

    def addMenu(self, menuBar):
        self.config(menu=menuBar)

    def setGeometry(self, width, height):
        self.geometry("%dx%d" % (width, height))

    def setCenterPlace(self):
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
         
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3 - windowHeight / 2)
         
        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))


class ThemedWindow(ThemedTk):

    GRID = "grid"

    def __init__(self, title=None):
        if title:
            super().__init__(className=title, theme="aquativo")
        else:
            super().__init__()
        self.layout = VERTICAL
        self.rowIndex = 0
        self.columnIndex = 0

        global _default_root
        _default_root = self
        self.statusbar = Label("状态栏", self)
        self.statusbar.setAnchor("w")
#         self.addWidget(self.statusbar, expand=YES)
        self.statusbar.pack(
            fill=BOTH, expand=NO, side=BOTTOM)

    def run(self):
        self.mainloop()

    def setLayout(self, layout):
        self.layout = layout

    def getLayout(self):
        return self.layout

    def addWidget(self, widget, row=None, column=None, expand=NO):
        if self.layout == VERTICAL:
            print(self.rowIndex, self.columnIndex,
                  widget.widgetName)
#             widget.grid(row=self.rowIndex, column=self.columnIndex, sticky="w" + "e")
#             self.rowIndex += 1
            widget.pack(fill=BOTH, expand=expand)
        elif self.layout == HORIZONTAL:
            #             widget.grid(row=self.rowIndex, column=self.columnIndex)
            #             self.columnIndex += 1
            widget.pack(fill=BOTH, expand=expand, side=LEFT)
        elif self.layout == self.GRID:
            if row == None:
                raise RuntimeError("row can not be None")
            if column == None:
                raise RuntimeError("column can not be None")
            widget.grid(row=row, column=column)

    def setTitle(self, title):
        self.title(title)

    def setTheme(self, theme_name):
        ThemedWidget.set_theme(self, theme_name)

    def showMaximized(self):
        #         w, h = self.maxsize()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.geometry("{}x{}".format(w, h))

    def showFullScreen(self):
        self.attributes("-fullscreen", True)

    def childrens(self):
        return self.winfo_children()

    def showMessage(self, msg):
        self.statusbar.setText(msg)

    def addMenu(self, menuBar):
        self.config(menu=menuBar)

    def setGeometry(self, width, height):
        self.geometry("%dx%d" % (width, height))


class VerticalLayout(ttk.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(text=text, master=parent,
                         relief='sunken')
        self.rowIndex = 0

    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text

    def setRowIndex(self, index):
        self.rowIndex = index

    def addWidget(self, widget):
        #         widget.grid(row=self.rowIndex, column=0, sticky='nsew')
        widget.pack(fill=BOTH, expand=YES)

    def childrens(self):
        return self.winfo_children()

    def getLayout(self):
        return VERTICAL


class HorizontalLayout(ttk.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(text=text, master=parent,
                         relief='sunken')
#         self.grid(column=0, row=0, sticky=(N, W, E, S))
#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(0, weight=1)
#         self.cnf = {"text":text, "bd":10, "height":300, "width":300}
        self.columnIndex = 0
#         self["bg"] = "blue"
#         self["bd"] = 5
#         self["height"] = 300
#         self["width"] = 300

    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text

    def setHeight(self, height):
        self["height"] = height

    def addWidget(self, widget):
        #         widget.grid(row=0, column=self.columnIndex, sticky='nsew')
        self.columnIndex += 1
        widget.pack(fill=BOTH, expand=YES, side=LEFT)

    def childrens(self):
        return self.winfo_children()

    def getLayout(self):
        return HORIZONTAL


class GridLayout(ttk.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(text=text, master=parent,
                         relief='sunken')
        self.empty_flag = True

    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text

    def addWidget(self, widget, row, column, rowspan=1, columnspan=1):
        #         self.columnconfigure(column, weight=1)
        #         self.rowconfigure(row, weight=1)
        if row == None and column == None and self.empty_flag:
            widget.grid(row=0, column=0, rowspan=rowspan,
                        columnspan=columnspan, sticky=N + S + W + E)
            self.empty_flag = False
        elif row != None and column != None:
            widget.grid(row=row, column=column, rowspan=rowspan,
                        columnspan=columnspan, sticky=N + S + W + E)

    def setWidth(self, width):
        self["width"] = width

    def childrens(self):
        return self.winfo_children()

    def getLayout(self):
        return "grid"


class Container(ttk.LabelFrame):

    def __init__(self, text=None, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(text=text, master=parent,
                         relief='sunken')
        self.layout = VERTICAL
        self.empty_flag = True

    def setLayout(self, layout):
        self.layout = layout

    def addWidget(self, widget, row=None, column=None, expand=NO):
        if self.layout == VERTICAL:
            widget.pack(fill=BOTH, expand=YES)
        elif self.layout == HORIZONTAL:
            widget.pack(fill=BOTH, expand=expand, side=LEFT)
        elif self.layout == "grid":
            if row == None and column == None and self.empty_flag:
                widget.grid(row=0, column=0, sticky="wens")
                self.empty_flag = False
            elif row != None and column != None:
                widget.grid(row=row, column=column, sticky="wens")

    def childrens(self):
        return self.winfo_children()

    def getLayout(self):
        return self.layout


class Label(ttk.Label):
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
        else:
            self["state"] = "disabled"

    def setAlignMent(self, alignMent):
        self["justify"] = alignMent

    def clear(self):
        self["text"] = ""

    def setHeight(self, height):
        self["height"] = height

    def setBackgroundColor(self, color):
        self["background"] = color

    def setAnchor(self, anchor):
        self['anchor'] = anchor

    def doubleClick(self, function):
        self.bind("<Double-Button-1>", function)


class PushButton(ttk.Button):
    """
    按钮
    """

    def __init__(self, text=None, parent=None):
        super().__init__(parent, text=text)
        self.cnf = {"text": text}

    def click(self, function):
        self["command"] = function

    def text(self):
        return self["text"]

    def setText(self, text):
        self["text"] = text

    def doubleClick(self, function):
        self.bind("<Double-Button-1>", function)


class RadioButton(ttk.Radiobutton):
    """
    单选按钮
    """

    def __init__(self, text=None, parent=None, RadioButtonGroup=None):
        super().__init__(parent, text=text)
        self["value"] = text
        if RadioButtonGroup:
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
        else:
            self.group.set(None)


class RadioButtonGroup(tk.StringVar):

    def __init__(self):
        super().__init__()


class CheckButton(ttk.Checkbutton):

    def __init__(self, text=None, parent=None):
        self.checkState = tk.BooleanVar()
        super().__init__(master=parent,
                         text=text, variable=self.checkState)
        self.items = {}

    def setChecked(self, boolean):
        if boolean:
            #             self.select()
            self.checkState.set(True)
        else:
            #             self.deselect()
            self.checkState.set(False)

    def setData(self, item, index=0):
        self.items[index] = item

    def data(self, index=0):
        return self.items[index]

    def isChecked(self):
        return self.checkState.get()


class LineEdit(ttk.Entry):

    def __init__(self, defaultValue=None, parent=None):
        super().__init__(master=parent)
        self.contents = tk.StringVar()
        self["textvariable"] = self.contents
        if defaultValue:
            self.contents.set(defaultValue)

    def text(self):
        return self.contents.get()

    def setText(self, text):
        self.contents.set(text)

    def alignment(self):
        return self["justify"]

    def clear(self):
        self.contents.set(None)

    def home(self):
        self.icursor(0)

    def isReadOnly(self):
        return self["state"] == "normal"

    def selectAll(self):
        self.select_range(0, len(self.get()))

    def setAlignment(self, alignment):
        self["justify"] = alignment

    def setReadOnly(self, boolean):
        if boolean:
            self["state"] = "disable"
        else:
            self["state"] = "normal"

    def setHideInput(self, char):
        self["show"] = char


class ListWidget(tk.Listbox):

    def __init__(self, parent=None):
        super().__init__(master=parent)

    def addItem(self, item):
        self.insert(END, item)

    def setSelectionModel(self, mode):
        self["selectmode"] = mode

    def addItems(self, items):
        self.insert(END, items)

    def insertItems(self, index, items):
        self.insert(index, items)

    def removeItemWidget(self, beginIndex, endIndex=None):
        self.delete(beginIndex, endIndex)

    def count(self):
        return self.size()

    def item(self, beiginIndex, endIndex=None):
        return self.get(beiginIndex, endIndex)

    def currentRow(self):
        return self.curselection()

    def itemDoubleClicked(self, command):
        self.bind('<Double-Button-1>', command)

    def setCurrentRow(self, index):
        self.activate(index)

    def currentItem(self):
        curselection = self.curselection()
        if len(curselection) == 1:
            return self.item(curselection[0])


class TreeWidget(ttk.Treeview):

    def __init__(self, parent=None):
        super().__init__(master=parent)

    def addTopLevelItem(self, item):
        self.insert('', 'end', id(item), text=item)

    def collapseItem(self, item):
        self.item(item, open=False)

    def expandItem(self, item):
        self.item(item, open=True)

    def currentItem(self):
        item = self.selesction()
        print("you clicked on ", str(item))
        return item

    def selectedItems(self):
        return self.selection()

    def addChildren(self, item, children):
        self.set_children(item, children)

    def clicked(self):
        self.bind("Button-1", self.currentItem)

    def doubleClick(self, command):
        self.bind("<Double-1>", command)

    def setHeader(self, text, width):
        self.heading(text, text=text)
#         self.column(text, width=width)

    def insertItem(self, rowIndex, record):
        self.insert("", rowIndex, values=record)

    def setColumns(self, columns):
        self["columns"] = columns


class ComboBox(ttk.Combobox):

    def __init__(self, parent=None):
        super().__init__(master=parent)
        self.value = tk.StringVar()
        self["textvariable"] = self.value
        self.values = []
        self["value"] = self.values

    def addItems(self, items):
        self.values.extend(items)
        self["value"] = self.values

    def addItem(self, item):
        self.values.append(item)
        self["value"] = self.values

    def count(self):
        return len(self.values)

    def clear(self):
        self.values.clear()

    def currentText(self):
        return self.values[self.current()]

    def setCurrentIndex(self, index):
        self.current(newindex=index)

    def setCurrentItem(self, item):
        index = self.values.index(item)
        if index:
            self.setCurrentIndex(index)

    def clicked(self, command):
        self.bind("<<ComboboxSelected>>", command)

    def setValues(self, values):
        self["value"] = values


class Menu(tk.Menu):

    def __init__(self, tearoff=None, parent=None):
        super().__init__(master=parent, tearoff=False)

    def addAction(self, text, function=None, returnCurText=False):
        if function:
            if returnCurText:
                self.add_command(
                    label=text, command=lambda: function(text))
            else:
                self.add_command(
                    label=text, command=function)
        else:
            self.add_command(label=text)

    def addSeparator(self):
        self.add_separator()

    def addMenu(self, text, menu):
        self.add_cascade(label=text, menu=menu)

    def removeAction(self, text):
        self.delete(text)


class kdSignal:

    def __init__(self):
        self.listerner = []
#         self.args_length = len(args)

    def emit(self, *args, **kwargs):
        for l in self.listerner:
            l(*args, **kwargs)

    def connect(self, function):
        self.listerner.append(function)


def addContextMenu(widget, menu):

    def popup(event):
        menu.post(event.x_root, event.y_root)

    widget.bind("<Button-3>", popup)


class PropertyEditor(ttk.Frame):

    def __init__(self, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(master=parent, relief='sunken')
        self.rowIndex = -1
        self.value_change_signal = kdSignal()

    def addLabel(self, text, row: int=None):
        widget = Label(text, self)
        if not row:
            self.rowIndex = self.rowIndex + 1
            row = self.rowIndex
        widget.grid(row=row, column=0)

    def _on_text_change(self, event):
        print("yes", event.widget.grid_info())
        widget = event.widget
        grid_info = widget.grid_info()
        lb = widget.master.grid_slaves(
            grid_info["row"], 0)
        if lb:
            if isinstance(widget, LineEdit):
                self.value_change_signal.emit(
                    lb[0].text(), widget.text())
            elif isinstance(widget, ComboBox):
                print("comboBox:", widget.currentText())
                self.value_change_signal.emit(
                    lb[0].text(), widget.currentText())

    def addAttribute(self, type, curValue, content=None, row: int=None):
        if not type or type == "text":
            widget = LineEdit(str(curValue), self)
            widget.bind("<Return>", self._on_text_change)
        elif type == "list":
            widget = ComboBox(self)
            widget.addItems(content)
            widget.setCurrentItem(curValue)

            widget.clicked(self._on_text_change)
        if not row:
            row = self.rowIndex

        if widget:
            widget.grid(row=self.rowIndex, column=1)

    def addRow(self, text, type, curValue, content=None, row: int=None):
        self.addLabel(text, row)
        self.addAttribute(type, curValue, content, row)

    def setRowIndex(self, index):
        self.rowIndex = index

    def addWidget(self, widget, row, column, rowspan=1, columnspan=1):
        self.columnconfigure(column, weight=1)
        self.rowconfigure(row, weight=1)
        widget.grid(row=row, column=column, rowspan=rowspan,
                    columnspan=columnspan, sticky=N + S + W + E)

    def addWidgetOnRow(self, widget):
        self.columnconfigure(self.columnIndex, weight=1)
        self.rowconfigure(self.rowIndex, weight=1)
        widget.grid(row=self.rowIndex, column=self.columnIndex,
                    rowspan=1, columnspan=1, sticky=N + S + W + E)
        self.rowIndex = self.rowIndex + 1
        print("self.rowIndex", self.rowIndex)

    def setWidth(self, width):
        self["width"] = width

    def childrens(self):
        return self.winfo_children()

    def clear(self):
        self.rowIndex = -1
        children = self.childrens()
        for child in children:
            child.destroy()


class Text(tk.Text):

    def __init__(self, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(master=parent)

    def append(self, text):
        self.insert(END, text)

    def clear(self):
        self.delete(1.0, "end")

    def setWidth(self, width):
        self["width"] = width

    def setHeight(self, height):
        self["height"] = height

    def setText(self, text):
        self.clear()
        self.append(text)

    def addVerticalScrollbar(self):
        scroll = tk.Scrollbar(self.master)
        scroll.pack(side=RIGHT, fill=Y)
        self.pack(side=LEFT, fill=Y)
        scroll.config(command=self.yview)
        self.config(yscrollcommand=scroll.set)


class Spinbox(tk.Spinbox):

    def __init__(self, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(master=parent, increment=1 , from_=-9999, to=9999)
        self.value = tk.IntVar()
        self.setTextvariable(self.value)
        self.setSingleStep(1)

    def maximum(self):
        return self["to"]

    def minimum(self):
        return self["from"]

    def setMaximum(self, maximum):
        self["to"] = maximum

    def setMinimum(self, minimum):
        self["from"] = minimum

    def setRange(self, minimum, maximum):
        self["from"] = minimum
        self["to"] = maximum

    def setSingleStep(self, step):
        self["increment"] = step

    def setValues(self, values:tuple):
        self["values"] = values

    def setValue(self, value:int):
        self.value.set(value)

    def value(self):
        return self.get()

    def singleStep(self):
        return self["increment "]
        
    def textFromValue(self):
        return str(self.get())

    def setTextvariable(self, textvariable):
        self["textvariable"] = textvariable


class Line(ttk.Separator):

    def __init__(self, orientation=HORIZONTAL, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        if orientation == VERTICAL :
            super().__init__(master=parent, orient="vertical")
        elif orientation == HORIZONTAL:
            super().__init__(master=parent, orient="horizontal")


class Scollbar(ttk.Scrollbar):

    def __init__(self, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(master=parent)    


class ScrolledWindow(tix.ScrolledWindow):

    def __init__(self, parent=None):
        if not parent:
            global _default_root
            parent = _default_root
        super().__init__(master=parent)
        self.w = self.window   
    
    def addWidget(self, widget):
        #         widget.grid(row=self.rowIndex, column=0, sticky='nsew')
        widget.pack(fill=BOTH, expand=YES)

    def childrens(self):
        return self.w.winfo_children()
