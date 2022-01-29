#!/usr/bin/env python
# -*-coding: utf-8 -*-

'''
   Toplama çıkarma yapacak modül
'''

print('modul eklendi')

# değişkenler
number = 10

numbers = [1,2,3]

person = {
    "name": "Ali",
    "age":"25",
    "city":"istanbul"
}

def SumFunc(x,y):
    '''
        Aldığı iki değişken toplamını döndürür
    '''
    print('Total:', x+y)
    
class Person:
    def speak(self): # metod 
        print('I am speaking...')