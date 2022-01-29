import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon


def window(): # create window
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('Python Simple GUI')
    win.setGeometry(100,100,500,250)
    win.setWindowIcon(QIcon('index2.png'))
    win.setToolTip('my app type')

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Name: ')
    lbl_name.move(50,30)

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Surname: ')
    lbl_name.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(120,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(120,70)

    def clicked(self):
        print('butona clicked! name : '+ txt_name.text()+ ' surmane : '+txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)




    win.show()
    sys.exit(app.exec_()) 

window()
