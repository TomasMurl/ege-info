from ipaddress import *

ip1 = ip_address("176.213.225.119")
ip2 = ip_address("176.213.195.58")

print(bin(int(ip1))[2:])
print(bin(int(ip2))[2:])

# 10110000.11010101.11100001.01110111 - ip1
# 10110000.11010101.11000011.00111010 - ip2
# 11111111.11111111.11000000.00000000 - mask
# 10110000.11010101.11000000.00000000 - net

net = ip_network("176.213.192.0/255.255.192.0")

c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:]
    if ip_2.count("1") % 2 == 0:
        c += 1
print(c)