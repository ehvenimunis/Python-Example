import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window(): # create window
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('Python Simple GUI')
    win.setGeometry(100,100,750,750)
    win.setWindowIcon(QIcon('index2.png'))
    win.setToolTip('my app type')


    win.show()
    sys.exit(app.exec_()) 

window()
