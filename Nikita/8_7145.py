alf = "0123456789"
c = 0
for n1 in "123456789":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                word = n1+n2+n3+n4
                if word.count("8") < 3:
                    if "18" not in word and "38" not in word and "58" not in word and "78" not in word and "98" not in word and "81" not in word and "83" not in word and "85" not in word and "87" not in word and "89" not in word:
                        c += 1
print(c)