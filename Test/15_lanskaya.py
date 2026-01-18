def find_dels(x):
    dels = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            dels.append(i)
            dels.append(x // i)
    return dels

def F(x, y):
    A = list(range(3, 106))
    B = find_dels(206)
    C = find_dels(y)
    if not C:
        return False
    return (x in C) <= ((x in A) and (not (x in B)))

for y in range(1000):
    if all(F(x, y) for x in range(-1000, 1000)):
        print(y)
        break