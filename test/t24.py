'''
Created on 2019年6月19日

@author: bkd
'''
from kdGUI import * 
app = Window("hao")
l1 = Label("bkd", app)
app.addWidget(l1)
l2 = Label("bkd2", app)
app.addWidget(l2)
l3 = Label("bkd3", app)
app.addWidget(l3)
s1 = Scollbar(app)
s1.pack(side=RIGHT, fill=BOTH, expand=YES)
app.run()
