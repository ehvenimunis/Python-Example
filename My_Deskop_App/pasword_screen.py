#!/usr/bin/env python
# -*-coding: utf-8 -*-

'''
   This module create window for add user info and there is a button in window
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from user_save import Data

class MyWindow(QMainWindow): # QMainWindow dan bir sınıf yaratıldı 
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('Log In')
        self.setGeometry(200,200,750,280) # window size 
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('my tooltip')
        self.var = Data()
        self.initUI() # define variables/buttons on screen

    def initUI(self):
        '''
            This function designed UI platform
        '''
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Name: ')
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Surname: ')
        self.lbl_surname.move(50,70)

        self.lbl_pasword = QtWidgets.QLabel(self)
        self.lbl_pasword.setText('Pasword: ')
        self.lbl_pasword.move(50,110)

        self.lbl_resut = QtWidgets.QLabel(self)
        self.lbl_resut.resize(500,100)
        self.lbl_resut.move(150,150)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)
        self.txt_name.resize(300,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150, 70)
        self.txt_surname.resize(300,32)

        self.txt_pasword = QtWidgets.QLineEdit(self)
        self.txt_pasword.move(150, 110)
        self.txt_pasword.resize(300,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Save')
        self.btn_save.move(590,30)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        '''
            This is a button function for saved user info
        '''
        self.minute = self.var.addUserInfo('Name: '+ self.txt_name.text()+ ' Surname: '+ self.txt_surname.text()+
         ' Pasword: '+ self.txt_pasword.text()) # Added user data on txt file
        self.lbl_resut.setText('Saved your info!'+ self.minute + '\n'+'Name: '+ self.txt_name.text()+
         '\nSurname: '+ self.txt_surname.text()+ '\nPasword: '+ self.txt_pasword.text())
        