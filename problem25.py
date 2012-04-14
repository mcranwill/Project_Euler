#! bin/usr/env python

import os
import sys

a=1
b=1
temp=0
new =0
i=2

while(1):
	new= a + b
	temp=a
	a= new
	b=temp
	i=i+1
	if((len(str(a)))==1000):
		print a
		print i
		sys.exit()
