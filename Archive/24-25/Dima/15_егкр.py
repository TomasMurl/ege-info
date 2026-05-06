B = range(36, 76)
C = range(60, 111)

min_len = 100000000000
for A_start in range(1, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end + 1)
        flag = True
        for x in range(90):
            F = (not(x in A)) <= ((x in B) == (x in C))
            if F == False:
                flag = False
        if flag == True:
            min_len = min(min_len, A_end - A_start)
print(min_len)