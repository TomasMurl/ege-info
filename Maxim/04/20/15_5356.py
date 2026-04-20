def f(x, y, A):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)

for A in range(100):
    # r = []
    # for x in range(100):
    #     for y in range(100):
    #         r.append(f(x, y, A))
    # if all(r):
    #     print(A)
    if all( f(x, y, A) for x in range(100) for y in range(100)):
        print(A)