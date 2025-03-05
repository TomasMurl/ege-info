def F(n):
    if n < 3:
        return 1
    if n > 2:
        return F((n+1) // 2) + 1

print(F(2025))