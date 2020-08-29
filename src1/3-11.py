string = ' Hello World'.strip() # baştaki ve sondaki boşluğu siler 
string1 = ' Hello World'.lstrip() # baştaki boşluğu siler 
string2 = ' Hello World'.rstrip() # sondaki boşluğu siler 

print(string)
print(string1)
print(string2)


string3 = 'Hello World'.count('e') # baştan sona kaç tane e harfi mevcut 
string4 = 'Hello World'.count('o', 0, 10) # 0 ile 10 arasında kaç tane o harfi var 

print(string3)
print(string4)

Website = 'https://www.btkakademi.gov.tr/portal/course/deliver/s-f-rdan-ileri-seviye-python-programlama-5877#!/play'
result = Website.startswith('https') # verilen kelime ile başlıyor mu 
print(result)

result1 = Website.endswith('play') # verilen kelime ile bitiyor mu 
print(result1)

result2 = Website.find('btk') # kelimenin bulunduğu index değerini gönderirir
print(result2)

result3 = Website.rfind('/') # sağdan başlayarak bak
print(result3) 

result4 = Website.index('.gov') # find metodu kelimeyi bulamaz ise -1 değerinin gönderir ama bu metod göndermez. 
print(result4)

kelime = 'Hello'
result5 = kelime.isalpha()
print("gelen veri alfabetik mi = ", result5)

kelime1 = '654654'
result6 = kelime1.isdigit()
print("gelen veri numerik mi = ", result6)



keyword = 'Yeni bir paste oluşturun'
result7 = keyword.replace(' ', '*') # boşluk gördüğün yere * koy 
print(result7)

result8 = result7.replace('*', '++', 10 ) # 10 index boyunca * ile ++ işaretlerini yer değiştir .
print(result8)

result9 = result8.split('++') # her bir kelimeyi karakter olarak ayor ve bir diziye ata 
print(result9[2])

result10 = result9[2].ljust(50, '#')
print(result10)
