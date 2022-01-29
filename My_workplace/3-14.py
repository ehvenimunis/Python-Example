numbers = [1,2,3,4,5,6,7,8,9]
letters = ['a', 'b', 'c', 'z']

val = min(numbers)
val1 = min(letters)
val2 = max(numbers)
val3 = max(letters)

print(val)
print(val1)
print(val2)
print(val3)


numbers[4] = 50 # eleman değiştirme 
print(numbers[4])

numbers.append(49)
numbers.insert(3,99) # indis vererek araya eleman eklemek 
print(numbers)

# eleman silme
numbers.pop()
print(numbers)
numbers.pop(0) # baştaki elemanı siler
numbers.pop(-1) # son elemanı sil 
numbers.remove(50) # verielen elemanı arayarak siler 
print(numbers)

# sıralama 
numbers.sort()
letters.sort()
print(numbers)
print(letters)

# ters sıralama 
numbers.reverse()
print(numbers)

# eleman sayma 
print(numbers.count(99))

# liste silme
numbers.clear()
print(numbers)
