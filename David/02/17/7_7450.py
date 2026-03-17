from math import *

k = 2
I = 48000
i = 34
v = 314572800
# Альбом = Треки + Заголовки

zagol = 110 * 1024 * 8 * 13
t = 42 * 60 + 20
treki = k * I * i * t

alb = zagol + treki
print(alb / v)