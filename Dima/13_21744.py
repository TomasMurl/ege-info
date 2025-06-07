from ipaddress import *

ip1 = ip_address("95.24.2.9")
ip2 = ip_address("95.24.3.10")
for mask in range(1, 32):
    net = ip_network(f"95.24.2.9/{mask}", 0)
    if ip2 not in net:
        print(net, mask)
        break

c = 0
net = ip_network("95.24.2.0/24")
for ip in net:
    ip2 = bin(int(ip))[2:]
    if ip2[-1] == '0':
        c += 1
print(c)