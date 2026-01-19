import ipaddress

net = ipaddress.ip_network("208.192.226.58/12", 0)
for ip in net:
    if str(bin(int(ip))[2:]).count("1") % 5 == 0:
        print(ip, sum(map(int, str(ip).split("."))))