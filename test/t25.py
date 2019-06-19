'''
Created on 2019年6月19日

@author: bkd
'''
from kdGUI import * 
app = Window("hao")
vl = ScrolledWindow(app)
# vl.addScrollbar()
l1 = Label("bkd", vl.w)
vl.addWidget(l1)
l2 = Label("bkd2", vl.w)
vl.addWidget(l2)
l3 = Label("bkd3", vl.w)
vl.addWidget(l3)
app.addWidget(vl)
# s1 = Scollbar(vl)
# s1.pack(side=RIGHT, fill=BOTH, expand=YES)
for i in range(15):
    vl.addWidget(Label("bkd" + str(i), vl.w))
    
app.run()
