#!/usr/bin/python
#Factorial without recursion
n = input("Enter n:")
n_factorial = 1
if n>=0:
	for i in range(2,n+1):
		n_factorial=i*n_factorial
	print str(n)+" factorial is "+str(n_factorial)
else:
	print "can't print factorial"