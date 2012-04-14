#! bin/usr/env python

import os

f = open("input.txt","r+")

line = f.readline()

accumulator =0
accumulator = accumulator + int(line)
while f:
	line = f.readline()
	accumulator = accumulator + int(line)
