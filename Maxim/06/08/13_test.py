from ipaddress import *

net = ip_network("124.128.112.142/255.255.192.0", False)

ip = net[1]
print(ip)
print(int(ip))
print(bin(int(ip)))
print(bin(int(ip))[2:])
print(bin(int(ip))[2:].zfill(32))