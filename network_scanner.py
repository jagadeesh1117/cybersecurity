import scapy.all as scapy

request = scapy.ARP()

request.pdst = 'x'
breadcast = scapy.Ether()

breadcast.dst = 'ff:ff:ff:ff:ff:ff'
request_broadcast = breadcast / request
clients = scapy.srp(request_broadcast, timeout = 1) [0]
for element in clients:
    print(element[1].psrc + "   "+ element[1].hwsrc)
