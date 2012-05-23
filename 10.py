#! bin/bash python

# array of flags to denote whether a prime or not.
iterator=0
a=list(range(2,2000000))
for x in a:
    comp=[]
    for y in a:
        comp.append(x*y)
    for z in comp:
        if z in a:
            a.remove(z)
print(a)
summation=0
#for x in a:
#	summation=summation+x
