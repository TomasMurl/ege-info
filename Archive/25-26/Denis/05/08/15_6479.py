def f(x, s, e):
    return (not ((369 <= x <= 3894) <= ((1381 <= x <= 2165) or (2643 <= x <= 3155)))) <= ((not (s <= x <= e)) <= (not (369 <= x <= 3894)))

ml = 100000000
for s in range(4000):
    print(s)
    for e in range(s + 1, 4000):
        if all(f(x, s, e) for x in range(4000)):
            l = e - s
            if l < ml:
                ml = l
print(ml)