def f(x, y, A):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)

for A in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            if not f(x, y, A):
                flag = False
    if flag:
        print(A)