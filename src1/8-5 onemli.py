mylist = [1,2,3]
myString = 'my string'

print(len(mylist))
print(len(myString))
print(type(mylist))
print(type(myString))


class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('film objesi silindi')

m = Movie('film adı','yönetmen adı',120) # obje oluşturduk


print(str(mylist))
print(str(m)) # movie nin ram üzerinde nerede bulunduğunu gösteren bir mesaj yayımlar 
print(len(m)) # yukarıda denedik bu metod çalışmıyordu. 

# objeyi ben del ile silmesem bile kullanılmadığında otomatik silindiği için del ile verilen mesajı yayımlar 
# python special methods diyerek aratırsan bu fonksiyonları bulursun 