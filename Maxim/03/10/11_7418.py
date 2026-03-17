from math import *

N_id = 10
N_p = 25
for n in range(1, 1000):
    i = ceil(log2(n))
    Id = N_id * i
    p = N_p * i
    u = ceil((Id + p) / 8 + 48)
    print(u * 1536, 120 * 1024)
    if u * 1536 == 120 * 1024:
        print(n)

u = 120 * 1024 / 1536
p_id = u - 48
print(p_id)
for n in range(1, 1000):
    i = ceil(log2(n))
    p_id_v = ceil(35 * i / 8)
    if p_id_v == p_id:
        print(n)