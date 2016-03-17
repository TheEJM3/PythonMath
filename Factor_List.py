import itertools

def factor_list(n):
	#running sum of factors
	factors = []
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
					factors.append(int(x))
				#if x and y are different
				else:
					#running sum adds factors
					factors.append(int(x))
					factors.append(int(y))
		else:
			break
	#function returns sum of factors
	factors.sort()
	return factors
print "List of a Number's Factors"
n = input("Enter Number: ")
print factor_list(n)