#!/usr/bin/python

from scapy.all import *
import os

def pkt_callback(pkt):
    if IP in pkt:
        if pkt[IP].dst == '10.0.0.1' and 'request' in pkt.summary():
            #os.system("echo \"10.0.0.1\" > output.txt")
            os.system("sta1 is roaming...")
            os.system("~/mininet-wifi/util/m sta1 wpa_cli -i sta1-wlan0 roam 00:00:00:00:00:02")
sniff(iface="sta1-wlan0", prn=pkt_callback, filter="icmp", store=0)
