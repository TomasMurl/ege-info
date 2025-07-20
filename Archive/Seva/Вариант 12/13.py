from ipaddress import *

ip1 = ip_address("154.63.206.129")
ip2 = ip_address("154.63.100.75")
print(bin(int(ip1))[2:])
print(bin(int(ip2))[2:])

# 10011010001111111100111010000001 - ip1
# 10011010001111110110010001001011 - ip2
# 11111111111111110000000000000000 - mask
# 10011010001111110000000000000000 - subnet
c = 0
net = ip_network("154.63.0.0/255.255.0.0")
for ip in net:
    ip_2 = bin(int(ip))[2:]
    summa_1 = ip_2.count("1")
    if summa_1 % 2 == 0:
        c += 1
print(c)