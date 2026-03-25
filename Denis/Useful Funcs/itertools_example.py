from itertools import product, permutations

# Комбинации с повторениями
alf = 'АБВ'
l = 2
words = product(alf, repeat=l)
# words = product('ABCDE', repeat=3)
# for w in words:
#     print(w)


# Комбинации без повторений
alf = 'АБВ'
l = 2
words = permutations(alf, l)
for w in words:
    w = ''.join(w)
    print(w, type(w))