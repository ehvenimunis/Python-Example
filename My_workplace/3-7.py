name = "Salih"
surname = "Aydogan"
age = 36

print('My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old. \n')

print('My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.')

greating = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.'
print(greating)

print(greating[0]) # ilk karakter ,
print(len(greating)) # krarakter sayısı 
print(greating[len(greating) - 1]) # son karakter 
print(greating[-1]) # son karakter 

print(greating[2:6])
print(greating[:15])
print(greating[15:])
print(greating[2:40:2]) # 2 den 40 değerine kadar 2 eleman aralıklarla ilerler 