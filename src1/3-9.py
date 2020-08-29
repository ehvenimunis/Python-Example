website = "muhammed salih aydoğan"


result = website[::]
result1 = website[::-1]

print(result)
print(result1)

s = "12345" * 5
print(s)
print(s[::5])   # 5 karakterde bir eleman almasını isteriz

kelime = 'Hello world'
# w harfini büyük hale getirelim 
new_kelime = kelime[0:6] + 'W' + kelime[-4:]    # birinci metod
new_kelime1 = kelime.replace('w', 'W')          # ikinci metod

print(new_kelime)
print(new_kelime1)