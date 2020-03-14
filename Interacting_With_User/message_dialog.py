#step 1. First, we need to import the GUI library:
from PyQt5.QtGui import *

#step 2. Then, we'll create the message dialog:
msg=QMessageBox()
#msg=QgsMessageBar()

#step 3. Next, we'll set the message we want to display:
msg.setText("This is the first message")

#step 4: call execution method to display the message box
msg.show()
