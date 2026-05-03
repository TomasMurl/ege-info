from itertools import combinations

P = range(25, 65)
Q = range(40, 116)
def f(A_s, A_e, x):
    return (x in P) <= (((x in Q) and (not (A_s <= x <= A_e))) <= (not (x in P)))

min_len = 1000000000
for c in combinations(range(200), 2):
    if all(f(c[0], c[1], x) for x in range(200)):
        min_len = min(min_len, c[1] - c[0])
print(min_len)