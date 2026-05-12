def f(x, s, e):
    return ((not( 52 <= x <= 105)) and (not (0 <= x <= 53)) and (not (s <= x <= e))) <= (x ** 2 > 303601)

min_len = 100000000000
for s in range(-5, 1000):
    for e in range(s + 1, 1000):
        if all(f(x, s, e) for x in range(1000)):
            l = e - s
            if l < min_len:
                min_len = l
print(min_len)