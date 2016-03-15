#Matt Parker's Pi Day Sing Along

#Edward J. McLean III
#Pi Day 2016!
#Raymond, NH

#Matt Parker made a YouTube vid about calculating Pi by hand
#using an infinite sum that tends towards pi.  The sum is:
#1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11... infinity.
#He did the first 10 fractions by hand ending on ...-1/19 and
#the sum was 3.04.  I wanted to know exactly how many fractions
#it would take to get a decimal accurate to 314 digits of pi.

#Using the script below, I figured out that the difference 
#between the sum and pi is slightly less than 1/# of fractions. For 
#example, the sum of the first 1,000,000 fractions in the series
#differs from pi by < 1/1,000,000 or .000001.

import math
from decimal import *
#precision will be good for first billion iterations
getcontext().prec = 10
#number of decimal points match precision
pi = Decimal(3.1415926536)
#variable used as running total of factors
runsum = Decimal(0.0)
#starts on 2 because -1^x will return + on each odd fraction
x = 2
#variable used for periodic, printed updates
y = 1
#iterations will stop at this amount
max = input("Enter Max Iterations: ")
#screen output at each time this amount is reached
z = input("Enter Update Rate: ")
#main loop:
for n in xrange((x-2), max):
	#returns next fraction then sums the previous fractions with current
	runsum = runsum + (((-1)**x)*(Decimal(1.000)/(x+(x-3))))
	#updates current count
	y = y + 1
	#updates current x value
	x = x + 1
	#if current count matches update rate, print update
	if y == z + 1:
		print "x =", x-2
		print "Current sum of factors =", runsum*4
		print "Difference between sum and pi=", Decimal(runsum*4) - pi
		y = 1
#when completed, print final values
print "x =", x-2
print "Current sum of factors =", runsum*4
print "Difference between sum and pi=", Decimal(runsum*4) - pi