#step 1. First, we need to import the GUI library:
from PyQt5.QtGui import *

#step 2: Next, we initialize the dialog:
qid=QInputDialog()


#step 3: Now, we set the window's title, label text, editing mode, and default text:
title="Enter Your name"
label="Name:="
mode=QLineEdit.Normal
default="<Your Name Here>"

#step 4: We configure the dialog while capturing the user input and the return
#code in variables:
text,ok=QInputDialog.getText(qid,title,label,mode,default)

#step 5: When the dialog appears, type in some text and click on the OK button.
#step 6: Now, we print the user input to the console:
print(text)

