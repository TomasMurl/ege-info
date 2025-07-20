def f(a, x):
    Q = range(12, 77)
    P = range(5, 48)
    R = range(58, 99)
    return (x in Q) <= ((not (x in P)) <= (((not (x in R)) and (not (x in a))) <= (not (x in Q))))

min_len = 1000000000000
for a_start in range(0, 500):
    for a_end in range(a_start + 1, 501):
        a = range(a_start, a_end + 1)
        if all(f(a, x) for x in range(-500, 500)):
            min_len = min(min_len, a_end - a_start)
            if (a_end - a_start) == min_len:
                print(a, min_len)
print(min_len)