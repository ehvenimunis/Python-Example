# Yöntem 1
# import math
# import math as islem    // bu yazım ile math yerine islem yazarka kütüphane kullanılabilir 

# value = dir(math)
# value = help(math)        // tüm metodlarını yazdırır
# value = help(math.factorial)
# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# value = islem.factorial(5)

# Yöntem 2
# from math import *    

def sqrt(x):
    print('x :'+ str(x))

from math import factorial,sqrt,ceil   # math kütüphaneinin yazılan metodlarını kullanmak için sadece 

# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)

print(value)