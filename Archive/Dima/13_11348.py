from ipaddress import *

ip = ip_address("119.83.208.27")
ip_net = ip_address("119.83.192.0")

print(bin(int(ip))[2:].zfill(32))
print(bin(int(ip_net))[2:].zfill(32))