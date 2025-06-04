def f(x, A):
    B = range(36, 76) # [36, 37, 38, 39 ... 75]
    C = range(60, 111)
    return (not (x in A)) <= ((x in B) == (x in C))

min_A = 10000000000000
for A_start in range(0, 200): 
    for A_end in range(A_start + 1, 201):
        A = range(A_start, A_end + 1) # [2; 4] -> [2, 3, 4] -> len = 3 -> 4 - 2 = 2
        if all(f(x, A) for x in range(-500, 500)):
            min_A = min(len(A) - 1, min_A)
print(min_A)