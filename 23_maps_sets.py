#!/usr/bin/python
def square(n):
	return n*n
value = [1,2,3,4]
numbers = map(square,value)
print numbers
set_numbers =set(numbers)
print set_numbers