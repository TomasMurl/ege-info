alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# print([[p, x, y, z, w] for p in range(10, 27) for x in alf[:p] for y in alf[:p] for z in alf[:p] for w in alf[:p]] if int(f"{y}07{x}", p)+int(f"{w}{y}9{z}", p)==int(f"{z}{x}{y}{x}{y}", p))

for p in range(10, 27):
    for x in alf[:p]:
        for y in alf[:p]:
            for z in alf[:p]:
                for w in alf[:p]:
                    flag = True
                    word = f"{x}{y}{z}{w}"
                    for i in word:
                        if word.count(i) > 1:
                            flag = False
                            break
                    if int(f"{y}07{x}", p)+int(f"{w}{y}9{z}", p)==int(f"{z}{x}{y}{x}{y}", p) and flag == True:
                        print(p, int(f"{x}{y}{z}{w}", p))
                        break