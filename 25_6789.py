import re
c = 0
for i in range(123405, 10 ** 8):
    if re.fullmatch(r"12[\d]*34\d5", str(i)) and i % 2025 == 0:
        print(i, i // 2025)