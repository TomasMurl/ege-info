from itertools import product

count_words = 0
cnt = 1
for w in product("ВЕКОТЦ", repeat=6):
    w = ''.join(w)

    if cnt % 2 == 1 and "Е" not in w and "К" not in w and w.count('О') == 2 and w.count('Ц') == 1:
        count_words += 1
    cnt += 1
print(count_words)