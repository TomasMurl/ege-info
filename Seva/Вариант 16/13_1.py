from ipaddress import *

ip1 = ip_address("176.213.225.119")
ip2 = ip_address("176.213.195.58")

print(bin(int(ip1))[2:])
print(bin(int(ip2))[2:])

print(int("11100000", 2))