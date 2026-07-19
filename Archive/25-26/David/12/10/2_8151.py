# И - and
# ИЛИ - or
# = - ==
# Импликация (->) - <=
# Не - not

print("x y z w F")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = w and (not((x <= y) <= (y == z)))
                if F == 1:
                    print(x, y, z, w, 1)