def find_del(n):
    dels = []
    flag = False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            if i != 9 and str(i)[-1] == '9':
                flag = True
                dels.append(i)
            if n // i != 9 and str(n // i)[-1] == '9':
                flag = True
                dels.append(n // i)
    return [flag, dels]

c = 0
for i in range(800001, 10 ** 10):
    result = find_del(i)
    if result[0] == True:
        print(i, min(result[1]))
        c += 1
    if c == 5:
        break