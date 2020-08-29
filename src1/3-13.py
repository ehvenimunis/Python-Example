key = ['elma', 'armut', 'erik']


#ilk ve son eleman 
result = key[0]
result1 = key[-1]
print(result)
print(result1)

# boyut 
print(len(key))

# eleman değiştirme 
key[-1] = "şeftali"
print(key[-1])

# eleman arama 
result2 = 'şeftali' in key  # şeftali key listesinin elemanı mıdır??
print(result2)

# sondan birinci eleman nedir??
result3 = key[-2]
print(result3)

# aralıklı yazdır 
result4 = key[0:2]
print(result4)
result5 = key[-2:]
print(result5)

print(key)
key[-1:] = ['muz', 'ananas']
print(key)

result6 = key + ['kavun'] 
print(result6)

# eleman silemek 
del key[-1:-1] 
print(key)


# elemanları tersten yazdırmak 
print(key[::-1])


