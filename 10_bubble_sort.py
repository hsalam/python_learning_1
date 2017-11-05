#!/usr/bin/python
a = [2,4,1,6,7,2,5,1]
print "array: "+str(a)
n = len(a)
for i in xrange(n-1):
	for j in xrange(n-i-1):
		if (a[j]>a[j+1]):
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
	print "Array after iteration %d is %s"%(i,str(a))
print "array :"+str(a)