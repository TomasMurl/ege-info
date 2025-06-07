from ipaddress import *

for mask in range(1, 32):
    net = ip_network(f"84.32.84.32/{mask}", 0)
    ip_max = bin(int(net[-2]))[2:]
    if ip_max.count("1") == 19:
        print(mask)