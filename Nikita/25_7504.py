def find_M(n):
    M = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            M = i + n // i
            return M
    return M

c = 0
for i in range(900000, 0, -1):
    M = find_M(i)
    if len(str(M)) > 2:
        if str(M)[-3:] == "112":
            print(i, M)
            c += 1
    if c == 5:
        break