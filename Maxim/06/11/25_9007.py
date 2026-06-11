from fnmatch import fnmatch

# 1. 1, 2, 3, 4, 5, 6, 7 ...
# 2. 271, 542, 813, ...
for n in range(271, 10 ** 8 + 1, 271):
    if fnmatch(str(n), '12??15*6'):
        print(n, n // 271)