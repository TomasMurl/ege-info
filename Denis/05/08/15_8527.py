def f(x, s, e):
    return (25 <= x <= 64) <= (((40 <= x <= 115) and (not (s <= x <= e))) <= (not (25 <= x <= 64)))

ml = 10000000000
for A_start in range(200):
    for A_end in range(A_start + 1, 200):
        if all(f(x, A_start, A_end) for x in range(200)):
            l = A_end - A_start
            if l < ml:
                ml = l
print(ml)