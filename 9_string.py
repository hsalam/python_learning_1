#!/usr/bin/python

#pgm to enter n number of strings and display them with no duplicates. Also to display the duplicate strings
list_names = []
duplicates = []
input_limit = raw_input("Enter the limit : ")
for i in range(0,int(input_limit)):
	list_names.insert(i,raw_input("Enter name "+str(i+1)+" : "))
# duplicate_list = list_names
# for item in duplicate_list:
# 	count = 0
# 	for names in list_names:
# 		if(cmp(item,names)==0):
# 			count+=1
# 			duplicate_list.remove(names)
# 	if (count > 1):
# 		print "name "+item+" occured "+str(count)+" number of times"
# 	else:
# 		print item
for i in xrange(int(input_limit)):
	count = 0
	if list_names[i] not in duplicates:
		for j in xrange(int(input_limit)):
			if list_names[i] == list_names[j]:
				count += 1
				duplicates.insert(i,list_names[i])
		if count>1:
			print "%s occured %d" %(list_names[i], count)
		print list_names[i]