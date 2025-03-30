from ipaddress import *

ip_in_network = ip_network("115.198.0.0/255.254.0.0")

c = 0
for ip in ip_in_network:
    ip_2 = bin(int(ip))[2:]
    if ip_2.count('1') % 5 == 0:
        c += 1
print(c)

int(chislo, 6)