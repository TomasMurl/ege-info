max_len = ""
for n in range(204):
    s = "1" * n + "2" + "1" * (203 - n)
    while "111" in s or "222" in s:
        if "111" in s:
            s = s.replace("111", "22", 1)
        else:
            s = s.replace("222", "11", 1)
    print("Текущее значение длины - ", len(s))
    print("Максимальное которое мы находили - ", len(max_len))
    if len(s) > len(max_len):
        max_len = s
print(max_len)
