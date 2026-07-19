def F(n):
    if n < 3:
        return 3
    else:
        return 2 * n + 6 + F_n[n - 2]

F_n = [None] * 4000

for i in range(len(F_n)):
    F_n[i] = F(i)

print(F_n[3027] - F_n[3023])