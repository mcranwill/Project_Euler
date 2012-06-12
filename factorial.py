#! bin/bash python

def factorial(i):
	product=1
	while(i>0):
		product*=i
		i=i-1
	return product

print(factorial(10))
