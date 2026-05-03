from itertools import combinations

B = range(36, 76)
C = range(60, 111)
def f(A_start, A_end, x):
    return (not (A_start <= x <= A_end)) <= ((x in B) == (x in C))

min_len = 1000000000000

for c in combinations(range(200), 2):
    if all(f(c[0], c[1], x) for x in range(200)):
        min_len = min(min_len, c[1] - c[0])
print(min_len)