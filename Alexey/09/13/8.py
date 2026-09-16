from itertools import permutations, product

# a = product('ЦВЕТОК', repeat=6)
a = permutations('ЦВЕТОК', 6)

for i in a:
    i = ''.join(i) # tuple
    print(i)