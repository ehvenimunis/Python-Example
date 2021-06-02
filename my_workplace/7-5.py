# map 

def kareAl(num): return num ** 2


numbers = [1,2,3,4,5,6]

result = map(kareAl, numbers)
print(result) # bu bize bir adres yazdırır 
result1 = list(map(kareAl, numbers))
print(result1) # bu iste sonuç yazdırır

# veya yazdırma işlemi şu şekilde yapılır 
for item in map(kareAl, numbers):
    print(item)



# eğer tek bir işlem yapılacakasa ayrıca bir fonksiyon yazmak yerine ' lamda ' kullanılır 
result2 = list(map(lambda num: num ** 3, numbers))
print(result2)

# farklı bir kullanım 
kareAL1 = lambda num: num ** 4
p = list(map(kareAL1, numbers))
print(p)

print("\n")


# filter fonksiyonu kullanımı 
# içine gelen syıların sadece çift olanlarını döndürür 
def check_even(num) : return num % 2 == 0    # gönderilen sayının modunu alır true veya false gönderiri 

result3 = list(filter(check_even, numbers))
result4 = list(filter(lambda num: num % 2 == 0, numbers)) # bu da aynı sonucu verecektir.
print(result3)
print(result4)