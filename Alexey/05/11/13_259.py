from ipaddress import *

ip1 = ip_address('11.156.152.142')
ip2 = ip_address('11.156.157.39')

for m in range(2, 32):
    net = ip_network(f'11.156.152.142/{m}', False)
    if ip2 in net:
        print(m)
