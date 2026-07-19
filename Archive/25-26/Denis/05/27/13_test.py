from ipaddress import *

# ip = ip_address('23.12.171.214')
# print(ip)
# print(int(ip))
# print(bin(int(ip))[2:])
# print(bin(int(ip))[2:].zfill(32))

# net = ip_network('NET_IP/MASK')
net = ip_network('240.144.182.134/255.255.248.0', False)
for ip in net:
    print(ip)