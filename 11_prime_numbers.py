#!/usr/bin/python
#pgm to check if a number is prime or not
number = input("Enter a number :")
if number > 1:
	for i in range(2,number):
		if(number%i==0):
			print "Number is not prime"
			break
	else:
		print"Number is prime"
else:
	print "Number is not prime"
