
tuple = (0,0)
tuple1 = (2,2)
tuple2 = (5,5)
tuple3 = (7,7)

listem = []
listem.append(tuple)
listem.append(tuple1)
listem.append(tuple2)
listem.append(tuple3)


# icinde_mi(x, y, cember_merkez_x, cember_merkez_y, yaricap)
def icinde_mi(a, b, c, e):
    print("aaa")
    for p in c:
        print("bbb")
        f = pow(a-p[0], 2) + pow(b-p[1], 2)
        mesafe = pow(f, 0.5)
        if(mesafe <= e):
            return 'evet içinde'
        else:
            pass
    
    return 'dışında'

print(str(icinde_mi(7.0, 5.0, listem, 1)))