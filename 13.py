#! bin/bash python

# array of flags to denote whether a prime or not.
primeTest= [0]
for i in range(2000000):
	primeTest.append(1)

primes=[2]
primeIndex=0
iterator=0
while (iterator < 500):
	li=1
	#iterate through primeTest
	while (li < len(primeTest)):
		if(primeTest[li] == 0):
			continue
		elif((li+1) % primes[primeIndex] == 0):
			primeTest.insert(li,0)
		pass
		li=li +1
	#store next prime number
	i=0
	while(primeTest[i] == 0 and i < 2000000):
		i = i+1
	
	if(i<2000000):
		primes.append(i+1)
	else:
		break
	pass
	iterator= iterator + 1

print(primes)
