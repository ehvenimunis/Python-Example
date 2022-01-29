# fonksiyon paramaetreleri 

def changeName(n):
    n = 'salih'

name = 'aydoğan'

changeName(name)
print(name) # name değişkeni değişmedi çünkü iki değişken ayrı ayrı adreslerde tutulmaktadır. 


# referance type
def change(n): # listenin bir kopyası çıkartılmasın sadece o adresteki eleman güncellensin istedik 
    n[0] = 'kerem'

isim = ['salih', 'gümüş']
change(isim) # değişkenin adresini göndermiş olduk 
print (isim)


# slicing işlemi (parçalama)
n = isim[:] # slicing
n[0] = 'enis'
print(isim, n) # isim dizisinin değişmediğini görürüz. bu şekilde orjinal listeyi değiştirmemiş oluruz.  dizisinin değişmediğini görürüz. bu şekilde orjinal listeyi değiştirmemiş oluruz. 



# bu da kullanışlı bir yapı 
def add(a, b, c = 5): # c değeri gönderilmediyse 5 olarak kullan 
    return sum((a,b,c))

print(add(1,2,3))
print(add(5,5))


def add1(*params):
    return sum((params))

print(add1(1,2,3,8,3,3)) # bu kullanımda sınırsız değer gönderilebilir 


def add2(*params):
    print(type(params))
    sum = 0 
    for n in params:
        sum = sum + n
    return sum

print(add2(1,2,3,8,3,3)) # gönderdiğimiz veri aslında bir tuple



# dictionaryi fonksiyona gönderme 

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))

displayUser(name = 'Salih', age = 23, city = 'istanbul') # bu bir dictionaary tipinde değişkendir. 



# asd
def myfunc (a, b, * args, **kwards):
    print(a)
    print(b)
    print(args) # tuple
    print(kwards) # dictionary 

myfunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')

