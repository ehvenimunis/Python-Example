
# verilen kelimeyi istenen sayıda yazdırır
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('merhaba ben salih\n', 10)



# liste oluşturan fonk 
def  listeyeCevir(*params):
    liste = []

    for param in params:
        liste.append(param)
    
    print('oluşan liste : ', liste)

listeyeCevir(10,20,30,40, "klmn")


print('\n')

# asal sayı bulan fonk 
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1: 
            for i in range(2 , sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

print('sayı giriniz!')
sayi1 = int(input('sayı 1 : '))
sayi2 = int(input('sayı 2 : '))
asalSayilariBul(sayi1, sayi2)


 