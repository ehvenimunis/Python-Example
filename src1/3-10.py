message = 'muhammed. salih Aydoğan'

message = message.upper() # tüm harfleri büyük yazar 
message1 = message.lower() # tüm harfleri küçük yazar 
message2 = message.title() # sadece kelimelerin ilk harfleri büyük 
message3 = message.capitalize() # sadece cümlenin ilk harfi büyük yazdırılır
message4 = message.strip() # başlangıçtaki boşluk karakterini kaldırır
message5 = message.split() # cümleyi parçalara ayırır
message6 = message.split('.') # noktalardan itibaren ayırır
print(message)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message6[1])

 
index = message1.find('aydoğan') # verilen kelimenin indisini bulacaktır 
print(index)

isFound = message.startswith('M') # cümle M ile mi başlıyor 
print(isFound)

isFound = message.endswith('N') # cümle N ile mi bitiyor 
print(isFound)

message1 = message1.replace('aydoğan' , 'Aydoğan') # değişim 
print(message1)

message1 = message1.center(50) # 50 karakterlik konteyner açıp elemanı merkeze yazdırır 
print(message1)

message1 = message1.center(50, '-')
print(message1)