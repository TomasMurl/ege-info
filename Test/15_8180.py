from itertools import combinations

def F(x, A):
    A = range(A[0], A[1])
    return (not (x in A)) <= ((x in B) == (x in C))

min_len = 10000000
combs = combinations(range(200), 2)
for A in combs:
    if all(F(x, A) for x in range(500)):
        min_len = min(A[1] - 1 - A[0], min_len)

print(min_len)