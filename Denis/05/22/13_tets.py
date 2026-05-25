from ipaddress import ip_address

print(bin(int(ip_address('111.81.208.27')))[2:].zfill(32))
print(bin(int(ip_address('111.81.192.0')))[2:].zfill(32))

# print(int('11011001', 2))
# print(int('00001000', 2))
# print(int('11110100', 2))
# print(int('00000000', 2))