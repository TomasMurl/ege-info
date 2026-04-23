from itertools import combinations

def f(x, A):
    return (25 <= x <= 64) <= (((40 <= x <= 115) and (not (A[0] <= x <= A[1]))) <= (not (25 <= x <= 64)))

m = 999999999999
for A in combinations(range(200), 2):
    if all( f(x, A) for x in range(200) ):
        m = min(m, A[1] - A[0])
print(m)