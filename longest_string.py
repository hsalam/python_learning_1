#!/usr/bin/python
string1 = raw_input("Enter string 1:")
string2 = raw_input("Enter string 2:")
len1 = len(string1)
len2 = len(string2)
if(len1>len2):
	print("String 1 is the largest")
elif(len2>len1):
	print("String 2 is the largest")
else:
	print("Both strings are equal")