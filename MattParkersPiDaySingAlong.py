import math
from decimal import *
getcontext().prec = 315
pi = Decimal(3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660632)
runsum = Decimal(0.0)
x = 2
y = 1
while Decimal(runsum*4) - pi != Decimal(0.00):
	while y < 1000001:
		runsum = runsum + (((-1)**x)*(Decimal(1.000)/(x+(x-3))))
		x = x + 1
		y = y + 1
	print "x =", x-2
	print "Difference =", Decimal(runsum*4) - pi
	y = 1
print "x =", x-2
print "Difference =", Decimal(runsum*4) - pi
print "runsum*4 =", runsum*4
print "It will not be 314 digits precise until you add 1/", (2*(x-2)-1)