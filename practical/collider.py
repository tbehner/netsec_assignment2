#!/usr/bin/env python3
import random
import hashlib
import time

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

prefix_length = 20
offset = 2

l_bound = offset
u_bound = offset + prefix_length

try:
  start_time = time.clock()
  while True:
    bits = bytes_to_bits(64)
    a, b = randbit_tuple(bits)
    hash_a = hash_bin(a)
    hash_b = hash_bin(b)
    if hash_a[l_bound:u_bound] == hash_b[l_bound:u_bound]:
      end_time = time.clock()
      print("Found after {} seconds!".format(end_time - start_time))
      break
except KeyboardInterrupt:
  print("Bye")
