from ipaddress import ip_address

print(bin(int(ip_address("111.81.200.27")))[2:].zfill(32))
print(bin(int(ip_address("111.81.192.0")))[2:].zfill(32))

print( '.'.join(map(lambda x: str(int(x, 2)), '11111111.11111111.11110000.00000000'.split('.'))) )

# 01101111010100011100100000011011
# *
# 11111111111111111111000000000000
# =
# 01101111010100011100000000000000
#
# 00 / 11 / 01 / 10