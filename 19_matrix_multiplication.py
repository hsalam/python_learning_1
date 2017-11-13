#!/usr/bin/python
#Matrix multiplication
m = input("Enter m :")
n = input("Enter n :")
p = input("Enter p :")
q = input("Enter q :")
if (n==p):
	A = [[0 for i in xrange(n)] for j in xrange(m)]
	B = [[0 for i in xrange(q)] for j in xrange(p)]
	C = [[0 for i in xrange(q)] for j in xrange(m)]
	for i in xrange(m):
		for j in xrange(n):
			A[i][j]+=input("Enter element A[%d][%d] : " %(i,j))
	for i in xrange(p):
		for j in xrange(q):
			B[i][j]+=input("Enter element B[%d][%d] : " %(i,j))
	for i in xrange(m):
		for j in xrange(q):
			for k in xrange(p):
				C[i][j]+=A[i][k]*B[k][j]
	print "Matrix after multiplication of A & B is \n %s" %C
else:
	print "Total number of columns in 1st matrix and number of rows in 2nd matrix should be equal"