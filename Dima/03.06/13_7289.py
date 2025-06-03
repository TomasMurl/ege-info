from ipaddress import *

ip1 = ip_address("211.188.211.49")
ip2 = ip_address("211.188.200.115")
print(bin(int(ip1))[2:])
print(bin(int(ip2))[2:])
print(2 ** 13)
ip_net = "11010011101111001100000000000000"
mask = "11111111111111111110000000000000"
mask = ".".join([str(int(mask[i:i+8], 2)) for i in range(0, len(mask), 8)])
ip_net = ".".join([str(int(ip_net[i:i+8], 2)) for i in range(0, len(ip_net), 8)])
print(mask, ip_net)

c = 0
net = ip_network(f"{ip_net}/{mask}")
for ip in net:
    if bin(int(ip))[2:].count("1") % 2 == 1:
        c += 1
print(c)