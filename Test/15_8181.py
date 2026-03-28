def F(x,y):
    return (x >= 9) or (2 * x < y) or (x * y < A)

for A in range(1000):
    if all(F(x,y) for x in range(1000) for y in range(1000)):
        print(A)
        break