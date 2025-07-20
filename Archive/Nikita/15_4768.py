P = range(1, 99)
Q = range(25, 43)
min_len = 1000000

for start in range(-50, 120):
    for end in range(start, 121):
        A = range(start, end+1)
        flag = True
        for x in range(0, 100):
            F = (x in Q) <= (((not (x in P)) and (x in Q)) <= (x in A))
            if F == False:
                flag = False
        if flag == True:
            min_len = min(min_len, len(A) - 1)
print(min_len)