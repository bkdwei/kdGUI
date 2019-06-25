'''
Created on 2019年6月19日

@author: bkd
'''
import time, threading

from kdGUI import *


def run():
    for i in range(10000):
        time.sleep(1)
        print(i)
        p.setValue(i * 1000)

        
app = Window("abk")
p = Progressbar(app)
app.addWidget(p)
p.setMaximum(10000)
p.setOrientation("vertical")
p["mode"] = "determinate"
# p.start(1)
t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

app.run()
