#! usr/bin/python

i=1
accumulator=0
while (i < 1001):
	accumulator += i**i
	i= i +1

y=len(str(accumulator))
my_answer=str(accumulator)
new_accumulator=''
i=0
while(i<10):
	new_accumulator += my_answer[y-1-i]
	i = i+1
print new_accumulator
print accumulator
