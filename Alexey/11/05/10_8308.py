from ipaddress import *

net = ip_network('192.168.12.207/255.192.0.0', False)
for ip in net:
    ip_2 = bin(int(ip))[2:]
    if ip_2.count('0') == ip_2.count('1'):
        print(ip)