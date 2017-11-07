#!/usr/bin/python
a = raw_input("Enter value of a:")
b = raw_input("Enter value of b:")
print type(a)
c = b+a
print "c is "+c
print type(c)
if b>a:
  print "b is greater than a"
elif a==b:
  print "a is equal to b"
else:
  print "a is greater than b"
print "program execution completed"
