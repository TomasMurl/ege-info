from itertools import product

# Подготовка, алфавит и формирование слов
alf = sorted("ПАРУС")
words = product(alf, repeat=5)

# Вся логика
c = 0
for word in words:
    w = "".join(word)
    c = c + 1
    if w[0] != 'У':
        continue
    if 'АА' in w:
        continue
    print(c, w)
    break