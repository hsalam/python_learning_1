#!/usr/bin/python
#Fibonacci series
limit = input("Enter limit:")
a = 0
b = 1
count = 0
if limit<=0:
 print "Can't print fibonacci series"
elif limit==1:
	print a
else:
	while(count<limit):
		print str(a)
		c = a+b
		a = b
		b = c
		count+=1