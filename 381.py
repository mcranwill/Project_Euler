#! /bin/bash python

def S(p,k_floor,k_top):
	summation=0
	i=k_floor	
	while(i<=k_top):
		summation= summation + factorial(p-i)
		i=i+1
	return (summation % p)

	
def factorial(i):
	product=1
	while(i >1):
		product =product*i 
		i=i-1
	return product
	
i=5
accumulat=0
while(i < 98 and i >=5):
	accumulat= accumulat + S(i,1,5)
	i= i + 1

print(accumulat)
