def f(A_start, A_end, x):
    return (not (A_start <= x <= A_end)) <= ((36 <= x <= 75) == (60 <= x <= 110))

min_len = 1000000000000
for i in range(200):
    for j in range(i + 1, 200):
        if all(f(i, j, x) for x in range(200)):
            min_len = min(min_len, j - i)
print(min_len)