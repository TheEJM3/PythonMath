def sigma(n):
	#running sum of factors
	runSum = 0
	#range from 1 to sqrt
	for x in xrange(1, int(n**.5+1)):
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
	#function returns sum of factors
	return int(runSum)

def factorize(n):
	if n<=2:
		return []
	sieve=[True]*(n+1)
	for x in range(3,int(n**0.5)+1,2):
		for y in range(3,(n//x)+1,2):
			sieve[(x*y)]=False
	primelist = [2]+[i for i in range(3,n+1,2) if sieve[i]]

	primeFactors = []
	for x in primelist:
		if n == 1:
			break
		while n%x == 0:
			n = n/x
			primeFactors.append(int(x))
	factorization = [[p,primeFactors.count(p)] for p in set(primeFactors)]
	factorization.sort()
	return factorization
	
def multiplicities(n):
	if n<=2:
		return []
	sieve=[True]*(n+1)
	for x in range(3,int(n**0.5)+1,2):
		for y in range(3,(n//x)+1,2):
			sieve[(x*y)]=False
	primelist = [2]+[i for i in range(3,n+1,2) if sieve[i]]

	primeFactors = []
	for x in primelist:
		if n == 1:
			break
		while n%x == 0:
			n = n/x
			primeFactors.append(int(x))
	factorization = [[p,primeFactors.count(p)] for p in set(primeFactors)]
	factorization.sort()
	
	multi = []
	for [x, y] in factorization:
		if y == 1:
			multi.append(x+1)
		else:
			multi.append(((x**(y+1))-1)/(x-1))
	return multi