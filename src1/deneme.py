import math

# list = (25)
# print(list)
# distance = []
# i = 0
# for i in range(0, 720, 15):
#     distance.append(i)

# print(len(distance))
# print(distance)

# Python3 code to demonstrate 
# shift last element to first  
# using list slicing and "+" operator 
  
# # initializing list
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8] 
  
# # printing the original list 
print ("The original list is : " + str(test_list)) 
  
# # using list slicing and "+" operator 
# # shift last element to first 
test_list = test_list[-2:] + test_list[:-2]  
  
# # printing result 
print ("The list after shift is : " + str(test_list)) 

# i = 0
# i = int(15 / 7.5)
# print(i)

# for i in range(49):
#     print(i)

# print(math.cos(math.pi))
# print(math.cos(180))

tuple = (1,2)
tuple1 = (2,3)
tuple2 = (4,5)
tuple3 = (6,7)

listem = []
listem.append(tuple)
listem.append(tuple1)
listem.append(tuple2)
listem.append(tuple3)

print ("\nThe list after shift is : " + str(listem)) 
print(str(listem[::-1]))
# listem = [] # elemanlarını yok ettik 
# print(str(len(listem)))
# print(str(list(listem)))


# for i in range(49):
#      print(i)
#      while(1):
#         break