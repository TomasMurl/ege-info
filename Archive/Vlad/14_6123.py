alf = "0123456789ABCDEFGHIJKLMNOPQ"

for i in range(8, len(alf)):
    alf_i = alf[:i]
    for x in alf_i:
        for y in alf_i:
            if int("1"+x+"77",i)+int(x+x+"77",i) == int(y+"0"+y+y,i):
                print(i, x, y)
                print(int(y+x+y+x,i))