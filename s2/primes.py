#!/usr/bin/env python

prime = True
for n in range(2, 10):
  if 11 % n == 0:
    print "11 is not prime!"
    prime = False 
    break
if prime:
  print "11 is prime!"
