alf = "ВУАЛЬ"
c = 0
for n1 in "ВУАЛ":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1+n2+n3+n4+n5
                    flag = True
                    if any(word.count(i) != 1 for i in alf) or "ЬУ" in word or "ЬА" in word:
                        flag = False
                    if "ЬУ" in word or "ЬА" in word:
                        flag = False
                    if flag:
                        c += 1
print(c)
                    