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