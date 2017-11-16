#!/usr/bin/python
s = raw_input("Enter string :") 
""" The wrap() function wraps a single paragraph in text (a string) so that every line is 
width characters long at most. It returns a list of output lines.

The fill() function wraps a single paragraph in text and returns a single string containing 
the wrapped paragraph."""

import textwrap
size = input("Enter n:")
print textwrap.wrap(s,size)
print textwrap.fill(s,size)
sub_string = raw_input("Enter a substring whose count is required : ")
print "Count of string %s is %s" %(sub_string,str(s.count(sub_string)))
print "The string after swapping cases is %s" %s.swapcase()
print "After applying reversed() function, the string becomes  %s" %reversed(s)
print "After applying str(reversed()) function, the string becomes  %s" %str(reversed(s))
print "After applying list(reversed()) function, the string becomes  %s" %list(reversed(s))
print "After applying s.lower() function, the string becomes  %s" %s.lower()