from itertools import *

def check(s):
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    return s

for n in range(1, 100):
    flag = False
    alf = "0" * 39 + "1" * n + "2" * 39
    combinations = permutations(alf)
    for stroka in combinations:
        check_string = ">" + "".join(stroka)
        result_string = check(check_string)[:-1]
        summa_cifr = sum([ int(i) for i in result_string ])
        if summa_cifr ** 0.5 % 1 == 0:
            print(n, summa_cifr)
            flag = True
            break
    if flag:
        break
        