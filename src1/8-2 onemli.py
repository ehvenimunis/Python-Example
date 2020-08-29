# class


class Person:
    # attributes (özellik - öz nitelik)
     # class attributes 
    adress = 'no information'

    # constructor ( yapıcı metod)
    # init metodu oluşturulan her bir obje için çalıştırılır 
    # burada self yerine herhangibir şey de yazılabilir sorun değiş. önemli olan ilk parametrede yer almasıdır 
    def __init__(self, name, year): # obje üzerine herhangi bir değeri aktarmak için self kullanacağım. virgülden sonra yazdıklrım eklemek istediğim özellikler olacaktır. 
        # bu kısım object attributes olacaktır
        self.name = name
        self.year = year
    

    # method



# object (instance)
p1 = Person('salih', 1997) # iki obje tanımladık 
p2 = Person('kerem', 1998)

print(p1) # objeleri yazdırınca farklı adreste bulunan Class yani Person tipinde bir şey görürüz
print(p2)
print(p1.name)
print(p1.year)
print(f'p2 name : {p2.name} year : {p2.year} adress : {p2.adress}') # burada class seviyesindeki attributes e de ulaşıldı 



# attributes change 
p1.name = 'muhammed'
p2.adress = 'mecidiye'
print(p1.name)
print(p2.adress)


# NOT : obje ilk oluşturulduğunda mutlaka tanımlanmasını istediğimiz özellikleri __init__ içerisinde yazarız 
    # Ama sadece istenildiğinde kullanılacak özelliklei class seviyesinde attributes olarak tanımlarız 