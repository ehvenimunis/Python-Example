# Döngüler

numbers = [1,2,3,55,8]

for i in numbers:
    print(i)

for i in numbers:
    print('hello')




names = ['salih', 'ahmet', 'kerem']
for name in names:
    print(f'my name is {name}')


# string ifadeler aslında bir karakter dizisidir
# bu sözün manasını görelim 
key = 'asaf emre'
for n in key:
    print(n)





tuple = [(1,2), (3,4), (5,6)]
for t in tuple:
    print(t)

for a,b in tuple:
    print(a)
    print(b)


d = {'k1':1, 'k2':2}
for item in d:
    print(item)

for item in d.items():
    print(item)

for anahtar,değer in d.items():
    print(anahtar, değer)