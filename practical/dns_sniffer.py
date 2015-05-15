#!/usr/bin/env python
import pcap
import dpkt

def handler(ts, pkt, d):
  udpPkt = dpkt.udp.UDP(pkt)
  data = udpPkt.data

  print "Received ", data, " at ", ts

pc = pcap.pcap()
pc.setfilter('udp')
pc.loop(handler)


