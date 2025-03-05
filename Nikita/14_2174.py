n = 81 ** 17 + 3 ** 24 - 45
n_9 = ''
while n > 0:
    n_9 = str(n % 9) + n_9
    n = n // 9
print(n_9.count("8"))