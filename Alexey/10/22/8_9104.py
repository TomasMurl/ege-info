from itertools import product

c = 1
for w in product('ЕЛНОСЦ', repeat=6):
    w = ''.join(w) # if 'АИ' in w | w = ('A', 'B') | 'AB'
    if c % 2 != 0 and w[0] != 'Ц' and w[0] != 'Н' and w.count('Ц') == 1 and w.count('Н') == 1:
        print(c, w)
    c += 1
print(c)