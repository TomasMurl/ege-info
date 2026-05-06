alf = "0123456789AB"
c = 0
for n1 in "123456789AB":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    flag = True
                    word = n1+n2+n3+n4+n5
                    if word.count("7") != 1:
                        flag = False
                    counter_8 = word.count("9") + word.count("A") + word.count("B")
                    if counter_8 > 3:
                        flag = False
                    if flag:
                        c += 1
print(c)