#Fibonacci Sequence Generator

#Edward J. McLean III
#March 8th, 2016
#Raymond, NH

#Given a max number of iterations, the script will generate the 
#Fibonacci sequence from 1, 1 to the number related to the max
#iterations.  The last number generated is then divided by the 
#second to last number generated.  It is said that this product
#will tend to the Golden Ratio.  For comparison, the final output
#of the script compares the product to the Golden Ratio.  Have
#a play around with it and see how close you get.  You may be
#dissapointed with the results.

#Enjoy!

from decimal import *
getcontext().prec = 50
actGRatio = 1.61803398874989484820458683436563811772030917980576
recursion = 1
fibOld = 1
fibNew = 1
fibOut = 1

n = input('Enter # of Recursions: ')

if (recursion < n + 1):
	while (recursion < 2):
		print "Recursion #%i =" % recursion, '{:,}'.format(fibOld)
		recursion = recursion + 1
		
if (recursion < n + 1):
	while (recursion < 3):
		print "Recursion #%i =" % recursion, '{:,}'.format(fibNew)
		recursion = recursion + 1
		
while (recursion < n + 1):
	fibOut = fibOld + fibNew
	print "Recursion #%i =" % recursion, '{:,}'.format(fibOut)
	fibOld = fibNew
	fibNew = fibOut
	recursion = recursion + 1
gRatio = Decimal(fibNew) / Decimal(fibOld)
print "Golden Ratio =", Decimal(gRatio)
diff = Decimal(actGRatio) - Decimal(gRatio)
print "Difference =", Decimal(diff) 