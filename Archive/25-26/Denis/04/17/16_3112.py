def F(n):
    if n <= 1:
        return 3
    else:
        return F(n - 1) + 2 * F(n - 2) - 5

a = F(22)
print(a)