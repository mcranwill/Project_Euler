#! usr/bin/python

x=999
y=999
temp=x*y

def rev(s):
	return s[::-1]

while((cmp(str(temp),rev(str(temp))))):
	y=y-1
	temp=x*y
	if(y < 900):
		y=999
		x=x-1
print(temp)
print(x)
print(y)
