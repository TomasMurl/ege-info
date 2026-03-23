alf = '0123456789ABCDEFGHI'

for x in alf:
    s = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if s % 18 == 0:
        print(x, s // 18)
