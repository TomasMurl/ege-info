def F(x, y, A):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)

for A in range(100):
    # flag_A = True
    # for x in range(100):
    #     for y in range(100):
    #         if F(x, y, A) == False:
    #             flag_A = False
    # if flag_A:
    #     print(A)
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
