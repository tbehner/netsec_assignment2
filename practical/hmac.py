#!/usr/bin/env python3
import sys
import hashlib
import argparse
import os

def lenbytes2lenbin(x):
  return x*8

def hex_to_bin(hex_string):
  return bin(int(hex_string,16))[2:]

def bin_xor(a,b):
  return bytes('{0:0{1}b}'.format(int(a,2)^int(b,2), len(a)),'utf-8')

def hmac(hash_function, block_size, ipad, opad, key, msg):
  rep_ipad = ipad * int(block_size/len(ipad)) 
  rep_opad = opad * int(block_size/len(opad)) 
  tmp = hash_function( bin_xor(key, rep_ipad) + msg )
  return hash_function( bin_xor(key,rep_opad) + tmp)

def hash_fkt(x): 
  return bytes(hashlib.sha512(x).hexdigest(), 'utf-8')

def pad_key(key, block_size):
  # compute binary representation of ascii string
  key = ''.join(format(ord(x),'b') for x in key)
  # pad the key with zeros
  padding_size = block_size - len(key)
  padded_key = '0' * padding_size + key
  return padded_key


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='HMAC')
  parser.add_argument('filename', metavar='FILENAME', type=str, 
      nargs=1, help='file to be authenticated')
  args = parser.parse_args()

  h = hashlib.new('sha512' )
  block_size = lenbytes2lenbin(h.block_size)

  # according to name2key for 'behner' as user
  key = pad_key('9b269f75c4', block_size)

  # ipad and opad according to the assignment
  ipad = hex_to_bin('93')
  opad = hex_to_bin('A5')

  if os.path.isfile(args.filename[0]):
    with open(args.filename[0],'rb') as ifile:
      msg = b''.join(ifile.readlines())
  else:
    msg = bytes(args.filename[0],'utf-8')
  print(hmac(hash_fkt, block_size, ipad, opad, key, msg).decode('utf-8'))
