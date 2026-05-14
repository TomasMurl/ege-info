from sys import setrecursionlimit
setrecursionlimit(258000)

def F(n):
    if n < 10:
        return 3
    else:
        return (n + 4) * F(n - 5)

print( (F(257487) // 683 + F(257477) // 67) // F(257472) )