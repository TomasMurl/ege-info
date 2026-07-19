def f(x, s, e):
    return (not ((36 <= x <= 384) <= ((131 <= x <= 215) or (243 <= x <= 355)))) <= ((not (s <= x <= e)) <= (not (36 <= x <= 384)))

ml = 100000000
for s in range(400):
    for e in range(s + 1, 400):
        if all(f(x, s, e) for x in range(400)):
            l = e - s
            if l < ml:
                ml = l
print(ml)