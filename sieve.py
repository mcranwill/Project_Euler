#! bin/bash python
a=list(range(2,1000))
for x in a:
    comp=[]
    for y in a:
        comp.append(x*y)
    print comp
    for z in comp:
        if z in a:
            a.remove(z)
print(a)
