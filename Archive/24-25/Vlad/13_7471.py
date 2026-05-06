import ipaddress

net = ipaddress.ip_network("106.184.0.0/255.248.0.0")

c = 0
for i in net:
    ip_2 = bin(int(i))[2:]
    if ip_2.count("1") % 2 != 0:
        c += 1

print(c)