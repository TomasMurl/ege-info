alf = "0123456789ABC"
for x in alf:
    n1 = int("615" + x + "483", 13)
    n2 = int("85996" + x + "262", 13)
    n3 = int("62421" + x, 13)
    n4 = int("45" + x + "61584" + x, 13)
    summa = n1+n2+n3+n4
    if summa % 12 == 0:
        print(summa // 12)
        break