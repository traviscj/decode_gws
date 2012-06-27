#!/usr/bin/python
# author: traviscj, june 27, 2012.
# tested on a D-Link DIR-615 B2 v2.25 firmware.
# this is a python translation of:
#     http://www.shulerent.com/2009/08/21/cracking-the-d-link-settings-file/
import sys

if len(sys.argv)!=2:
	print("usage: %s [gws filename]"%sys.argv[0])
	sys.exit(1)
f=open(sys.argv[1])
fstr = f.read()
decoded = []
for i in range(len(fstr)):
	thisch = ord(fstr[i])-(i%256)
	if thisch < 0:
		thisch += 256;
	decoded.append(chr(thisch))

print "".join(decoded)

