#! bin/bash python

import os

# array of flags to denote whether a prime or not.
primeTest= [0]
for i in range(50):
	primeTest.append(1)

primes=[2]
primeIndex=0
iterator=0
while (iterator < 20):
	if(iterator>0):
		primeIndex=primeIndex+1
	li=(primes[primeIndex]+1)
			
#	print(primes[primeIndex])
	#iterate through primeTest
	while (li < len(primeTest)):
		if(primeTest[li] == 0):
			pass
		elif((li+1) % primes[len(primes)-1] == 0):
			primeTest[li]=0
		#if(li==5):
		#	print 5
		#	print(primeTest[li])
		li=li +1
	#store next prime number
	if(primes[len(primes)-1]==3):
		primes.append(5)
		continue

	print primes[primeIndex]
	i= (primes[len(primes)-1])
	print i
	while(primeTest[i] == 0 and i < 20):
		if(primeTest[i]==0):
			i = i+1
#		print i
#		print primeTest[i]
	iterator= iterator + 1
	if(i<20):
		primes.append(i)
	else:
		break
	pass
print(primeTest)
print(primes)
print(len(primeTest))
