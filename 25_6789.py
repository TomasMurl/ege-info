import re
c = 0
for i in range(0, 10 ** 8, 2025):
    if re.fullmatch("12[\d]*34\d5", str(i)):
        print(i, i // 2025)