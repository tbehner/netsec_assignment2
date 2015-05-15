#!/usr/bin/env python3
import random
import hashlib
import time

import matplotlib
# don't show figures
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def bytes_to_bits(k):
  return 8*k

def randbit_tuple(bits):
  a = "{0:b}".format(random.getrandbits(bits))
  b = "{0:b}".format(random.getrandbits(bits))
  return (a,b)

def hash_value_hex(string):
  return hashlib.sha256(string.encode("utf-8")).hexdigest()

def hash_bin(string):
  return bin(int(hash_value_hex(string),16))

def plot_graph(prefix_length, data):
  plt.figure(num=None, figsize=(8, 8), dpi=300, facecolor='w', edgecolor='k')
  plt.title("Colliding Bits: %s" %(prefix_length))
  plt.xlabel('Steps', labelpad=10)
  plt.ylabel('Attempts until collission', labelpad=10)
  # plot graph
  plt.plot(data, color = '#2f9bdb', linestyle = '-', linewidth = 1)
  # save plot
  plt.savefig("%s.png" % (prefix_length))
  # close figure so that it doesn't need any memory anymore
  plt.close()

try:
  with open("Collider data.txt", "w") as f:
    f.write("Prefix Length\tStep\tTime\tTries\r\n")
    for prefix_length in [4,8,12,16,20]:
      results_time = []
      results_tries = []
      for i in range(5):
        print "Bits: %s Step: %s" % (prefix_length, i+1)
        offset = 2
        l_bound = offset
        u_bound = offset + prefix_length
        
        start_time = time.clock()
        tries_count = 0
        while True:
          tries_count += 1
          bits = bytes_to_bits(64)
          a, b = randbit_tuple(bits)
          hash_a = hash_bin(a)
          hash_b = hash_bin(b)
          if hash_a[l_bound:u_bound] == hash_b[l_bound:u_bound]:
            end_time = time.clock()
            f.write("%s\t%s\t%.8f\t%s\r\n" % (prefix_length, i, end_time - start_time, tries_count))
            results_time.append(end_time - start_time)
            results_tries.append(tries_count)
            break
      plot_graph(prefix_length, results_tries)
except KeyboardInterrupt:
  print("Bye")
