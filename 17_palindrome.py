#!/usr/bin/python
import sys
#pgm to check if a string is plaindrome or not
input_string = raw_input("Enter the string : ")
input_string = input_string.lower()
#reverse_string = input_string[::-1]
list_string = list(input_string)
length = len(input_string)

for i in range(length/2):
	if list_string[i]==list_string[length-1-i]:
		continue
	else:
		print "Not palindrome"
		sys.exit(1)
print "Palindrome"
