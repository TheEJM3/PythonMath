#Factors of a Number Squared

#Edward J. McLean III
#March 8th, 2016
#Raymond, NH

#This simple code prints all factors of a number squared.
#I wrote this one as a prototype for the ChristaNumbers.py
#script.  It might be helpful for someone else that needs
#a script like this, but a more universal function was 
#ultimately written for use in the ChristaNumbers.py script.

#Enjoy!

from decimal import *

n = long(input ("Enter a number: "))
square = n**2

for b in xrange(1, n + 1):
	a = square/float(b)
	check = (a).is_integer()
	if check == True:
		print "%i * %i = %i" % (a, b, square)