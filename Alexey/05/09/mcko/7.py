from ipaddress import *

net_ip = IPv4Address('192.168.108.157')
mask = IPv4Address('255.255.255.192')

print(bin(int(net_ip))[2:])
print(bin(int(mask))[2:])

print(int('11101', 2))