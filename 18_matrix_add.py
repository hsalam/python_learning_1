#!/usr/bin/python
x = input("Enter x:")
y = input("Enter y:")
A = [[0 for i in xrange(x)] for j in xrange(y)]
B = [[0 for i in xrange(x)] for j in xrange(y)]
C = [[0 for i in xrange(x)] for j in xrange(y)]
#print def(A)
for i in xrange(x):
	for j in xrange(y):
		A[i].insert(j,input("Enter element A[%d][%d]:" %(i,j)))
		A[i].pop()
for i in xrange(x):
	for j in xrange(y):
		B[i].insert(j,input("Enter elemenr B[%d][%d]:" %(i,j)))
		B[i].pop()
for i in xrange(x):
	for j in xrange(y):
		C[i].insert(j,A[i][j]+B[i][j])
		C[i].pop()
print C