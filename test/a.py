
from kdGUI import *


class kdGUIDesigner(Window):

    def __init__(self):
        super().__init__()

        self.PushButton_0 = PushButton('PushButton_0', self)
        self.addWidget(self.PushButton_0)


app = kdGUIDesigner()
app.run()
