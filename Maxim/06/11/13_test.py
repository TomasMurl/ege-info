from ipaddress import *

ip1 = ip_address("175.184.52.103")
ip2 = ip_address("175.184.48.0")

print(bin(int(ip1))[2:].zfill(32))
print(bin(int(ip2))[2:].zfill(32))

# IP * Mask = Адрес сети

# 10101111101110000011010001100111
# 11111111111111111111100000000000
# 10101111101110000011000000000000


# print(int('11110000', 2))