'''
Created on 2019年5月26日

@author: bkd
'''
from kdGUI import *
import time
from tkinter import VERTICAL
from ttkthemes import THEMES


def aa():
    print("in aa")
#     for theme in THEMES:
#         global win
#         win.setTheme(theme)
#         print("theme:" + theme)
#         time.sleep(5)
    global theme_index
    global tb_result
    win.setTheme(THEMES[theme_index])
    print(THEMES[theme_index])
    tb_result.setText(THEMES[theme_index])
    theme_index += 1


theme_index = 0
win = ThemedWindow("Java日志查看器")
# win.setLayout(HORIZONTAL)
win.setTheme(THEMES[0])

gl = GridLayout("导入和查询", win)
win.addWidget(gl)

# 第一行
pb_open = PushButton("打开日志文件", gl)
pb_open.click(aa)
lb_encoding = Label("编码格式", gl)
le_encoding = LineEdit("GB2312", gl)
pb_query = PushButton("查询", gl)
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
cb_debug = CheckButton("debug", gl)
cb_info = CheckButton("info", gl)
cb_warn = CheckButton("warn", gl)
cb_error = CheckButton("error", gl)
gl.addWidget(lb_level, 3, 0)
gl.addWidget(cb_debug, 3, 1)
gl.addWidget(cb_info, 3, 2)
gl.addWidget(cb_warn, 3, 4)
gl.addWidget(cb_error, 3, 5)

# 第五行
lb_method = Label("方法", gl)
le_method = LineEdit(None, gl)
lb_keyword = Label("关键字", gl)
le_keyword = LineEdit(None, gl)
gl.addWidget(lb_method, 4, 0)
gl.addWidget(le_method, 4, 1, 1, 2)
gl.addWidget(lb_keyword, 4, 3)
gl.addWidget(le_keyword, 4, 4, 1, 2)

vl = VerticalLayout("结果", win)
win.addWidget(vl)

tb_result = Label("ss", vl)
tb_result.setBackgroundColor("white")
statusbar = Label("状态栏", vl)
vl.addWidget(tb_result)
vl.addWidget(statusbar)

win.run()
