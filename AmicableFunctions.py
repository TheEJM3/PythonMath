def sig(n):
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

def fact(n):
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
	
def multi(n):
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
	
	multiplicities	= []
	for [x, y] in factorization:
		if y == 1:
			multiplicities.append(x+1)
		else:
			multiplicities.append(((x**(y+1))-1)/(x-1))
	return multiplicities
	
def prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True