from itertools import combinations

def f(x, A_start, A_end):
    return ((4 <= x <= 15) and (12 <= x <= 20)) <= (A_start <= x <= A_end)

min_len = 1000000000000
for c in combinations(range(30), 2):
    if all(f(x, c[0], c[1]) for x in range(30)):
        if c[1] - c[0] < min_len:
            min_len = c[1] - c[0]
print(min_len)