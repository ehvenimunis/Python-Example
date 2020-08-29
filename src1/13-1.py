# iteratörler

liste = [1,2,3,4,5,6]

# for i in liste: # biz farkında olmadan burada iteratör kullanıyoruz. döngüdeki liste iterabıl bir objedir. 
#     print(i)


iterator = iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# şimdi while döngü ile yazdıralım 

while True: # bu işlemi aslında for döngüsü bizim için yaparak elemanları yukarıda da görüldüğü gibi yazdırmaktadır. 
    try:
        element = next(iterator)
        print(element)
    except StopIteration: # eğer stop iteration hatası gelirse döngüden çık 
        break


# bu dersin devamı vardı bak