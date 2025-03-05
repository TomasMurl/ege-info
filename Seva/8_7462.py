alf = "012345678"
c = 0
for n1 in "12345678":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1+n2+n3+n4+n5
                    flag = True
                    if word.count("0") != 1:
                        flag = False
                    for i in range(len(word)-1):
                        if word[i] == "0" and word[i+1] in "1357":
                            flag = False
                        if word[i] in "1357" and word[i+1] == "0":
                            flag = False
                    if flag:
                        c += 1
print(c)