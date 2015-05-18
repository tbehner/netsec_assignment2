#!/usr/bin/env python
import pcap
import dpkt
import socket

pc = pcap.pcap()
pc.setfilter('udp')

for ts, pkt in pc:
  eth = dpkt.ethernet.Ethernet(pkt)
  ip = eth.data
  udp = ip.data
  if udp.dport != 53 and udp.sport != 53:
    continue

  try:
    dns = dpkt.dns.DNS(udp.data)
    if udp.sport == 53:
      for answer in dns.an:
        if answer.type == dpkt.dns.DNS_A:
          print 'Answer: ', answer.name, '\tIP Address: ', socket.inet_ntoa(answer.rdata)
    elif udp.dport == 53:
      print 'Query: ', dns.qd[0].name
  except:
    continue

