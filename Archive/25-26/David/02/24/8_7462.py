from itertools import product

alf = '012345678'
words = product(alf, repeat=5)

c = 0
for w in words:
    w = "".join(w)
    if w[0] == '0':
        continue
    if w.count('0') != 1:
        continue
    if '10' in w or '01' in w or '30' in w or '03' in w or '50' in w or '05' in w or '70' in w or '07' in w:
        continue
    c = c + 1
print(c)