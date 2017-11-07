#!/usr/bin/python

#pgm to enter n number of strings and display them with no duplicates. Also to display the duplicate strings
list_names = []
duplicates = []
no_duplicate_list = []
input_limit = raw_input("Enter the limit : ")
for i in range(0,int(input_limit)):
	list_names.insert(i,raw_input("Enter name "+str(i+1)+" : "))
for i in xrange(int(input_limit)):
	count = 0
	if list_names[i] not in duplicates:
		for j in xrange(int(input_limit)):
			if list_names[i] == list_names[j]:
				count += 1
				duplicates.insert(i,list_names[i])
		if count>1:
			print "%s occured %d" %(list_names[i], count)
			no_duplicate_list.insert(i,list_names[i])
print "List of strings with no duplicates :\n %s" %no_duplicate_list