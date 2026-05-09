def f(x, A_start, A_end):
    return ((4 <= x <= 15) and (12 <= x <= 20)) <= (A_start <= x <= A_end)

min_len = 1000000000000
for A_start in range(30):
    for A_end in range(A_start + 1, 30):
        if all(f(x, A_start, A_end) for x in range(30)):
            if A_end - A_start < min_len:
                min_len = A_end - A_start
print(min_len)