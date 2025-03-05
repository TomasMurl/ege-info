import ipaddress

net = ipaddress.ip_network("112.160.0.0/255.240.0.0")

c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:]
    if ip_2.count("1") % 5 == 0:
        c += 1

print(c)