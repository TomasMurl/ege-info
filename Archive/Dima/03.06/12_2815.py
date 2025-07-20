def red(s):
    while "111" in s:
        s = s.replace("111", "2", 1)
        s = s.replace("222", "1", 1)
    return s

for n in range(101, 10000):
    s = "1" * n
    result = red(s)
    if result == "2":
        print(n)
        break