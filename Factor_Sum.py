import itertools

def factor_sum(n):
	#running sum of factors
	runSum = 0
	#range from 1 to sqrt
	for x in itertools.count(1):
		if x < int(n**.5+1):
			#divides input by range
			y = n/float(x)
			#checks if calc returns int
			if (y).is_integer():
				#only counts each factor once
				if y == x:
					#running sum adds factors
					runSum = runSum + x
				#if x and y are different
				else:
					#running sum adds factors
					runSum = runSum + y + x
		else:
			break
	#function returns sum of factors
	return runSum
print "Sum of a Number's Factors"
n = input("Enter Number: ")
print factor_sum(n)