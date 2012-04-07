#! usr/bin/python

import os
import math
import sys

if (len(sys.argv) > 1):
	x = math.factorial(sys.argv[1])
else:
	x = math.factorial(100)
y=str(x)
accumulator=0
for i in range(len(y)):
	accumulator = accumulator + int(y[i])
print accumulator
print x
