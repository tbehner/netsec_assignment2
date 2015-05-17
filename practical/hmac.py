#!/usr/bin/env python3
import sys
import hashlib

def hex_to_bin(hex_string):
  return bin(int(hex_string,16))[2:]

def bin_xor(a,b):
  return '{0:0{1}b}'.format(int(a,2)^int(b,2), len(a)) 

def hmac(hash_function, block_size, ipad, opad, key, msg):
  rep_ipad = ipad * int(block_size/len(ipad)) 
  rep_opad = opad * int(block_size/len(opad)) 
  tmp = hash_function( bin_xor(key, rep_ipad) + msg )
  return hash_function( bin_xor(key,rep_opad) + tmp)

hash_fkt = lambda x : hashlib.sha512(x.encode("utf-8")).hexdigest()
# according to `Wikipedia <http://en.wikipedia.org/wiki/Secure_Hash_Algorithm>`
block_size = 1024
# according to name2key for 'behner' as user
key = '9b269f75c4'
key = ''.join(format(ord(x),'b') for x in key)
padding_size = block_size - len(key)
padded_key = '0' * padding_size + key
# ipad and opad according to the assignment
hex_ipad = '93'
hex_opad = 'A5'
ipad = hex_to_bin(hex_ipad)
opad = hex_to_bin(hex_opad)

msg = sys.argv[1]
print(hmac(hash_fkt, block_size, ipad, opad, key, msg))
