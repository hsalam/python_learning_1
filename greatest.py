#!/usr/bin/python
a = int(raw_input("Enter value of a:"))
b = int(raw_input("Enter value of b:"))
c = int(raw_input("Enter value of c:"))
if a>b and a>c:
	print("a is greatest")
elif b>a and b>c:
	print("b is greatest")
elif c>a and c>b:
	print("c is greatest")
else:
	print("All are equal")