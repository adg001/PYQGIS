#step 1. First, we must import both the GUI and QGIS core libraries:
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#step 2.Next, we create a custom class for our progress bar, including a method to increase
#the value of the progress bar:

class Bar(QProgressBar):
    value=0
    
    def increaseValue(self):
        self.setValue(self.value)
        self.value=self.value+1

#step 3. Now, we set the progress bar:
bar=Bar()

#step 4: Next, we set the progress bar's size and title:
bar.resize(300,40)
bar.setWindowTitle("Working..")

#step 5. Then, we initialize the timer, which will serve as the process we monitor:
timer=QTimer()

#step 6. Now,connect the the timer's timeout signal to the increaseValue method,
#which we created earlier. Whenever the timer finishes its countdown, it will emit the
#timeout signal and notify the increaseValue method.
timer.timeout.connect(bar.increaseValue)

#step 7. Now, we will start the timer, specifying an interval of 500 milliseconds. The timer will
#call its timeout() signal every 0.5 seconds:

timer.start(500)

#step 8. Finally, we show the progress bar and start the progress meter:
bar.show()