def primes(n):
	if n<=2:
		return []
	sieve=[True]*(n+1)
	for x in range(3,int(n**0.5)+1,2):
		for y in range(3,(n//x)+1,2):
			sieve[(x*y)]=False
	return [2]+[i for i in range(3,n+1,2) if sieve[i]]

	
print "List of a Number's Factors"
n = input("Enter Number: ")

primelist = primes(n)
print primelist
primeFactors = []

for x in primelist:
	if n == 1:
		break
	while n%x == 0:
		n = n/x
		primeFactors.append(int(x))
		
factorization = [[p,primeFactors.count(p)] for p in set(primeFactors)]

multiplicities = []

for [x, y] in factorization:
	if y == 1:
		multiplicities.append(x+1)
	else:
		multiplicities.append(((x**(y+1))-1)/(x-1))

print factorization
print multiplicities
print reduce(lambda x, y: x*y, multiplicities)