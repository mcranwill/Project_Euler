#! bin/usr/env python

import math
import os
import sys

def isTriplet(a, b, c):
	if(a<b and b < c):
		if(a**2 + b**2 == c**2):
			return 1
		else:
			return 0
	else:
		return 0
#END DEF

def isSolution(a,b,c):
	if(a+b+c == 1000):
		return 1
	else:
		return 0
#END DEF

a = 1
b = 1
c = 1

for i in range(1000):
	for j in range(1000):
		if(isTriplet(a,b,c)):
			if(isSolution(a,b,c)==1):
				print "answer is "
				print a
				print b
				print c
				print a*b*c
				sys.exit()
			else:
				b = b+1
				c = 1000 - a -b
		else:
			b= b+1
			c=1000 - a -b
	pass
	a = a + 1
	b = 1
	c = 1000 - a -b
pass


		
if(isTriplet(a,b,c)==1):
	print "true"
else:
	print "false"
