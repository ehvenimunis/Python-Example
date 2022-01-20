#!/usr/bin/env python
# -*-coding: utf-8 -*-

import time

'''
   This module create txt file for add user info
'''

class Data():
    def __init__(self) -> None:
        self.liste = []
            
    def addUserInfo(self, info):
        '''
            This function saved user info in txt file and returned running time 
        '''
        start = time.time()
        time.sleep(1)  
        with open("/home/salih/Documents/Python-Example/My_Deskop_App/newfile.txt","r",encoding='utf-8') as file:
            
            for i in file:
                self.liste.append(i)
            file.close()

            with open("/home/salih/Documents/Python-Example/My_Deskop_App/newfile.txt","w",encoding="utf-8") as file2:
                file2.write(info+'\n\t')
                for i in self.liste:
                    file2.write(i)
                file2.close()
                finish = time.time()
                print("This work " + str(finish-start-1.0) + " minute continued.")
                return "\nThis work " + str(finish-start-1.0) + " minute continued."
            

