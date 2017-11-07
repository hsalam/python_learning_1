#!/usr/bin/python
#pgm to display prime number between a range of numbers
lower = input("Enter lower range:")
upper = input("Enter upper range:")
if (lower==1 and upper==1) or lower>upper:
	print "Cannot display prime numbers"
#if(lower<=upper and lower>=1):
else:
	if lower==1:
		lower+=1
	for i in xrange(lower,upper+1):
		for j in range(2,i):
			if(i%j==0):
				print "%d is Not prime number" %i
				break
		else:
			print "%d is a prime number" %i
	
