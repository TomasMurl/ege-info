def F(n):
    if n <= 1:
        return 3
    if n > 1:
        return F(n-1) + 2 * F(n-2)-5

print(F(22))