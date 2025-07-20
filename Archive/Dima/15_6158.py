# ДЕЛ(n, m)  =>   n % m == 0

P = range(257, 357)
Q = range(5, 601)
R = range(59, 229)
min_A = 10000

for A_start in range(1, 700):
    for A_end in range(A_start + 1, 701):
        A = range(A_start, A_end)
        flag = True
        for x in range(1, 750):
            F = ((x in R) <= (x in A)) or (((x % 3 == 0) <= (x in P)) <= ( (x in Q) <= (x in A ) ) )
            if F == False:
                flag = False
        if flag:
            min_A = min( len(A) - 1, min_A )
print(min_A)