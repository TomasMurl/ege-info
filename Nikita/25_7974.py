from fnmatch import fnmatch
for i in range(0, 10 ** 9, 7863):
    if fnmatch(str(i), "?54*32*1"):
        sc = sum([int(c) for c in str(i)])
        print(i, sc)