from sys import setrecursionlimit
setrecursionlimit(260000)

def F(n):
    if n < 10:
        return 3
    else:
        return (n + 4) * F(n - 5)

print( str((F(257487) // 683 + F(257477) // 67) // F(257472))[-8:] )