#!/usr/bin/python
import sys
#to split a sentence and to count number of words in a sentence
input_string = raw_input("Enter the sentence :")
split_list = input_string.split()
print "no: of words="+str(len(split_list))
#print dir(a)		
#to print words in descending 
print "Printing words after reversing :"
for split in reversed(input_string.split()):
	print split