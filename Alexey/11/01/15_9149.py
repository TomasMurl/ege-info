def f(x, A):
    return ((not (290 <= x <= 750)) and (135 <= x <= 675)) <= (((not (x in A)) and (135 <= x <= 675)) <= (290 <= x <= 750))

min_len = 100000000
for A_start in range(1000):
    for A_end in range(A_start + 1, 1000):
        A = range(A_start, A_end + 1)
        if all(f(x, A) for x in range(1000)):
            min_len = min(A_end - A_start, min_len)

print(min_len)