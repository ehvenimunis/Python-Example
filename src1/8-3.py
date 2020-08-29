# class function


class Person:

    adress = 'no information'
  
    def __init__(self, name, year): 
        # bu kısım object attributes olacaktır
        self.name = name
        self.year = year
    

    # method
    def intro(self):
        print(f'Bu bir fonksiyon ve bu fonsiyon self parametresi aldığı için class içerisindeki attribute lere erişebilir örnek : {p1.adress} {p2.adress}')

# object (instance)
p1 = Person('salih', 1997) # iki obje tanımladık 
p2 = Person('kerem', 1998)

print(f'p2 name : {p2.name} year : {p2.year} adress : {p2.adress}') # burada class seviyesindeki attributes e de ulaşıldı 

# fonksiyon erişimi 
p1.intro()
p2.adress = 'Bilgi var' # değişim yapıldı
p2.intro()