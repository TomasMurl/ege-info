alf_19 = "0123456789ABCDEFGHI"
for x in alf_19:
    n1 = "55"+x+"36"
    n2 = x+"2724"
    n1 = int(n1, 19)
    n2 = int(n2, 19)
    if (n1 + n2) % 11 == 0:
        print((n1+n2)/11)
        break