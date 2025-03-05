ip = "192.168.0.1"
mask = "255.255.255.255"
net = ""
ip_2 = ".".join(map(bin[2:], map(int, ip.split("."))))
print(ip_2)