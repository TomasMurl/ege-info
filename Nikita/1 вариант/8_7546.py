alf = "0123456789ABCD"
c = 0
for n1 in "123456789ABCD":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1 + n2 + n3 + n4 + n5
                    flag = True
                    if word.count('9') != 1:
                        flag = False
                    if word.count('B') + word.count('C') + word.count('D') > 3:
                        flag = False
                    if flag:
                        c += 1
print(c)