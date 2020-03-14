#step 1. First, we need to import the GUI library:
from PyQt5.QtGui import *

#step 2: Next, we initialize the warning dialog:
msg=QMessageBox()

#step 3: Then, we set the warning message:
msg.setText("This is a warning message")

#step 4:Now, add a warning icon to the dialog that has an enumeration index of 2:
msg.setIcon(QMessageBox.Warning)

#step 5: Finally, we call the execution method to display the dialog:
msg.show()