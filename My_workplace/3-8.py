#string formatlama işlemleri 
name = 'selam'
surname = 'aydogan'
age = 36

print('my name is {}'.format(name))
print('my name is {} {}'.format(name, surname))
print('my name is {1} {0}'.format(name, surname)) # tersine çevirdim
print('my name is {y} {n}'.format(n = name, y = surname)) # harf kullanrarak yer değiştirme
print('my name is {} {} and I am {} years old.'.format(name, surname, age))

result = 200 / 700
print("the result is {r:1.4}".format(r = result)) # virgülden sonra 4 basamak bıraksın denildi 


print(f'my name is {name} {surname} and I am {age} years old.')