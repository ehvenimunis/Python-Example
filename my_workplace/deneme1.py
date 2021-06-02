# tuple = [(1,2), (3,4), (5,6)]
# for t in tuple:
#     print(t[0])

# for k in tuple:
#     print(k[1])

# # for a,b in tuple:
# #     print(a)
# #     print(b)


test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# for i in test_list:
#     for k in test_list1:
#         print(i, k)


# -------------------------------------------------
test_list3 = [0, 1, 2, 3, 4, 15, 6, 7, 8]
x = []


for i in range(len(test_list3)):
    tuple = (i, test_list3[i])
    x.append(tuple)

print(len(test_list3))
print(str(x))
print(len(x))


for i in x:
    print(i[1])


# ------------------------------------------
print(str(x))
x.pop(0)
x.pop()
print(str(x))