from itertools import combinations
from math import inf

def F(x, A):
    P = range(1381, 2165)
    Q = range(369, 3894)
    R = range(2643, 3155)
    return (not ((x in Q) <= ((x in P) or (x in R)))) <= (not (x in A) <= (not (x in Q)))

min_len_A = +inf
combs = combinations(range(5000), 2)
for comb in combs:
    start, end = comb
    # Внимание здесь, мы отдаем в функцию отрезок без последнего элемента
    # А наш код рассчитан так, что мы работаем с ним как с +1
    A = range(start, end + 1)
    if all(F(x, A) for x in range(5000)):
        leng = end - start
        if leng < min_len_A:
            min_len_A = leng
            print(start, end)
print(min_len_A)