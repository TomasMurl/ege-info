from itertools import permutations

c = 0
output = set()
for j in range(1, 5):
    stroka_def = "1" * 4 + "2" * j
    stroki = permutations(stroka_def)
    for stroka in stroki:
        result = "".join(stroka)
        if "111" not in result and "22" not in result and result.count("1") == 4:
            print(result)
            output.add(result)
print(len(output))