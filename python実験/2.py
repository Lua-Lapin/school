print("   | 1  2  3  4  5  6  7  8  9  ")
print("---+----------------------------")
line = " {0[0]} |{0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} "
list = [0]*10
for i in range(1,10):
    list[0]=i
    for k in range(1,10):
        if i*k//10 == 0 :
            list[k]=" "+str(k*i)
        else:
            list[k]=str(k*i)
    print(line.format(list))
