'''
Created on 2019年5月26日

@author: bkd
'''
from tkinter import VERTICAL
from kdGUI import *


def aa():
    print("in aa")


win = Window("Java日志查看器")
win.setLayout(VERTICAL)

gl = GridLayout("导入和查询", win)
win.addWidget(gl)

# 第一行
pb_open = Button("打开日志文件", gl)
lb_encoding = Label("编码格式", gl)
le_encoding = LineEdit("GB2312", gl)
pb_query = Button("查询", gl)
gl.addWidget(pb_open, 0, 0)
gl.addWidget(lb_encoding, 0, 3)
gl.addWidget(le_encoding, 0, 4)
gl.addWidget(pb_query, 0, 5)

# 第二行
lb_start = Label("开始时间", gl)
le_start = LineEdit("", gl)
lb_end = Label("结束时间", gl)
le_end = LineEdit("", gl)
gl.addWidget(lb_start, 1, 0)
gl.addWidget(le_start, 1, 1, 1, 2)
gl.addWidget(lb_end, 1, 3)
gl.addWidget(le_end, 1, 4, 1, 2)

# 第三行
lb_prefix = Label("线程号前缀", gl)
le_prefix = LineEdit("T", gl)
lb_thread_id = Label("线程号", gl)
le_thread_id = LineEdit("", gl)
gl.addWidget(lb_prefix, 2, 0)
gl.addWidget(le_prefix, 2, 1, 1, 2)
gl.addWidget(lb_thread_id, 2, 3)
gl.addWidget(le_thread_id, 2, 4, 1, 2)

# 第四行
lb_level = Label("日志级别", gl)
cb_debug = CheckBox("debug", gl)
cb_info = CheckBox("info", gl)
cb_warn = CheckBox("warn", gl)
cb_error = CheckBox("error", gl)
gl.addWidget(lb_level, 3, 0)
gl.addWidget(cb_debug, 3, 1)
gl.addWidget(cb_info, 3, 2)
gl.addWidget(cb_warn, 3, 4)
gl.addWidget(cb_error, 3, 5)
                  
win.run()

