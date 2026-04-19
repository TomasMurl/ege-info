a = [1, 2, 3]
# b = []
# for i in a:
#     b.append(i ** 2)
# print(b)

def f(n):
    return n ** 2

b = list(map(f, a))
print(b)

print('1231'[-2:])