P = range(13, 22)
Q = range(23, 36)
R = range(28, 39)

min_len = 10000

for start in range(-50, 100):
    for end in range(start + 1, 101):
        A = range(start, end)
        flag = True
        for x in range(0, 80):
            F = (not ((x in Q) <= ((x in P) or (x in R)))) <= ((not (x in A)) <= (not (x in Q)))
            if F == False:
                flag = False
        if flag == True:
            print(f"[{start}:{end-1}] - {len(A)-1}")
            min_len = min(min_len, len(A)-1)
print(min_len)

