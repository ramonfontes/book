#!/usr/bin/python

from scapy.all import *
import os

def pkt_callback(pkt):
    if IP in pkt:
        if pkt[IP].dst == '10.0.0.2' and 'request' in pkt.summary():
            #os.system("echo \"10.0.0.2\" > output.txt")
	    os.system("sta2 is roaming...")
            os.system("~/mininet-wifi/util/m sta2 wpa_cli -i sta2-wlan0 roam 00:00:00:00:00:03")
sniff(iface="sta2-wlan0", prn=pkt_callback, filter="icmp", store=0)
