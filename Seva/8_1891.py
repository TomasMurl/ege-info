alf = "ВЕСНА"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            word = n1 + n2 + n3
            flag = True
            # if word.count("А") < 1:
            #     flag = False
            if "А" not in word:
                flag = False
            if flag:
                c += 1
print(c)

            