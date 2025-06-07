def f(x, A):
    P = range(17, 59)
    Q = range(29, 81)
    return (x in P) <= (((x in Q) and (not (x in A))) <= (not (x in P)))

min_len = 10000000000000
for A_start in range(0, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end + 1)
        if all(f(x, A) for x in range(-100, 100)):
            leng = A_end - A_start
            min_len = min(min_len, leng)
print(min_len)