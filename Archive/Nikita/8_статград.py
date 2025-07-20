# def proverka(n):
#     result = []
#     while n > 0:
#         if n % 14 in result:
#             return False
#         result.append(n % 14)
#         n = n // 14
#     if len(result) < 8:
#         return False
#     return True

def perevod(n):
    result = []
    while n > 0:
        result.append(n % 14)
        n = n // 14
    return result[::-1]

print(perevod(738000000))

# c = 0
# for i in range(100000000, 738000001):
#     result = proverka(i)
#     if result:
#         c += 1
# print(c)