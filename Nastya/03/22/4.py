# 4.1
s = 0
for i in range(4, 65, 2):
    s = s + i ** 0.5  # (1/2)
print(s)

# 4.2
s = 0
i = 4
while i < 65:
    s = s + i ** 0.5
    i = i + 2
print(s)