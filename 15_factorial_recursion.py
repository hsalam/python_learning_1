#!/usr/bin/python
def rec_factorial(n):
	if(n>1):
		factorial = n*rec_factorial(n-1)
		return factorial
	else:
		return 1
N = input("Enter number :")
if N<0:
	print "Factorial of negative number doesn't exist"
else:
	print "factorial of ",N," is ",rec_factorial(N)
