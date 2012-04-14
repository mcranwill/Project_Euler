#! bin/usr/env python

import sys
import math

f = 2**1000

x=0
b = str(f)
print b
accumulator=0
for i in range(len(b)):
	accumulator = accumulator + int(b[x])
	x=x+1

print accumulator
