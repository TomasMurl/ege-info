from ipaddress import *

for m in range(32):
    net = ip_network(f'111.81.200.27/{m}', False)
    print(m, net)

print('1' * 20 + '0' * 12)