num1 = "24351"
num2 = "14325"
for p in range(6, 36):
    for q in range(6, 36):
        n1 = int(num1, p)
        n2 = int(num2, q)
        if n1 == n2:
            print(n1, p, q)