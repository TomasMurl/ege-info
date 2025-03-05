# Дел(n,m) =>  n % m == 0

for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        F = ((x % 2 == 0) <= (not (x % 3 == 0))) or (x + A >= 80)
        if F == False:
            flag = False
    if flag:
        print(A)
        break