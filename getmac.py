from scapy.all import *
import time
ip_range = "192.168.242.0/24"
 
arp_request = ARP(pdst=ip_range) 
ether = Ether(dst="ff:ff:ff:ff:ff:ff") 
packet = ether/arp_request
while(1):
    result = srp(packet, timeout=60, verbose=0)[0] 
    mac_addresses = []
    for sent, received in result:
        mac_addresses.append(received.hwsrc)
    from macdb import check_mac
    check_mac(mac_addresses)