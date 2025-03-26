from sys import setrecursionlimit
setrecursionlimit(1000000000)

def calc(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    if start >= 100:
        starsh = start // 100
    else:
        starsh = start // 10
    return calc(start + 1, end) + calc(start + start % 10, end) + calc(start + starsh, end)

print(calc(82, 95))