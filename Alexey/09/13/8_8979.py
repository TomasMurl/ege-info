from itertools import product

count_nums = 0
for w in product('0123456', repeat=5):
    w = ''.join(w)
    if w[0] != '0' and w.count('0') == 1 and w.count('1') <= 2:
        count_nums += 1
print(count_nums)