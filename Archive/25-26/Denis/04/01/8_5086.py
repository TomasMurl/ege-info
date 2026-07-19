from itertools import product
for c, w in enumerate(product('АПРСУ', repeat=5), start=1):
    w = "".join(w)
    if w[0] == "У" and "АА" not in w:
        print(c, w)
        break