my_list = [1,2,3,6]
my_list1 = ['one', 2, 2.1, True]

print(my_list)
print(my_list1)

my_list2 = my_list + my_list1
print(my_list2)
print(len(my_list2)) # eleman sayısı 


# listenin içine liste ekleme 
my_list3 = [my_list, my_list1]
print(my_list3)
print(my_list3[0][2])