#!/usr/bin/python
#Fibonacci series
limit = input("Enter limit:")
a=0
b=1
if limit==1:
	print a
elif limit==2:
	print str(a)+"\n"+str(b)
elif limit>2:
	print str(a)+"\n"+str(b)
	for i in range(2,limit):
		temp=b
		b=a+b
		a=temp
		print b
else:
 print "Can't print fibonacci series"
