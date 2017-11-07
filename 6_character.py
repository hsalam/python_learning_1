#/usr/bin/python
a = raw_input("Enter the character :")
print "list of valid attributes for %s is \n%s" %(a,dir(a))
length = len(a)
if length==1 :
	print "input is single character"
	if a.isdigit() :
		print "input is numeric"
	elif a.isalpha() :
		print "input is an alphabet"
else :
	print "input is not single character"