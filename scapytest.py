import psutil
import os
import scapy.all as scapy
import pandas as pd

io = psutil.net_io_counters(pernic=True)
# all_macs = {iface.values() for iface in io.items()}

print("sniff sent")
scapy.sniff(filter="icmp and host 66.35.250.251", count=2, timeout=10) #will run indefinitely until packets are found
print("timeout")
#dictionary to map connection to process
connection2pid = {}

psutil.net_connections()

def process_packet(packet):
    try:
        packet_connection = (packet.sport, packet.dport)
    except (AttributeError, IndexError):
        pass
    else:
        packet_pid = connection2pid.get(packet_connection)
        if packet_pid:
            if packet.src in all_macs: #if packet source is from our own mac
                #is outgoing traffic
                print("outgoing")
            else:
                #is incoming traffic
                print("incoming")
            print(pid)
            
def get_connections():
    global connection2pid
    
        
print(io)