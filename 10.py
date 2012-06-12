#! bin/bash python

# array of flags to denote whether a prime or not.
iterator=0
a=list(range(2,2000000))
for even in a:
	if(even % 2 == 0 and even > 2):
		a.remove(even)
for x in a:
    comp=[]
    for y in a:
        comp.append(x*y)
    for z in comp:
        if z in a:
	    a.remove(z)
	elif(z > a[-1]):
	    break
summation=0
for i in a:
	summation=summation+i
print(summation)
print(a)
if(len(a)>10001):
	print(a[10001])
