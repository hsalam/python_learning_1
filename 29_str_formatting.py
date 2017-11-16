#!/usr/bin/python
M, N = input("Enter M and N (both numbers should be odd and N should be twrice M :\n"), input()
for i in xrange(0,M/2):
	print (".|."*i).rjust((N-2)/2,"-")+".|." + (".|."*i).ljust((N-2)/2,"-")
print "WELCOME".center(N,"-")
for i in reversed(xrange(0,M/2)):
	print (".|."*i).rjust((N-2)/2,"-")+".|." + (".|."*i).ljust((N-2)/2,"-")