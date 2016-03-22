import itertools
import time

def primes(n):
	if n<=2:
		return []
	sieve=[True]*(n+1)
	for x in range(3,int(n**0.5)+1,2):
		for y in range(3,(n//x)+1,2):
			sieve[(x*y)]=False
	return [2]+[i for i in range(3,n+1,2) if sieve[i]]

def sigma(n):
	primeFactors = []
	for x in primelist:
		if n == 1:
			break
		while n%x == 0:
			n = n/x
			primeFactors.append(int(x))
	factorization = [[p,primeFactors.count(p)] for p in set(primeFactors)]
	multiplicities = [1]
	for [x, y] in factorization:
		if y == 1:
			multiplicities.append(x+1)
		else:
			multiplicities.append(((x**(y+1))-1)/(x-1))
	return reduce(lambda x, y: x*y, multiplicities)
	
print "List of a Number's Factors"
min = input('Enter Min Iterations: ')
max = input('Enter Max Iterations: ')
startTime = time.time()

print "Start Time:",time.strftime("%H:%M:%S", time.localtime(startTime))

if min < 3:
	min = 3
	
primelist = primes(max)

for n in itertools.count(min):
	if n < (max+1):
		sigman = sigma(n)
		m = (sigman-n)
		if m > n:
			sigmam = sigma(m)
			if sigman == m+n and m+n == sigmam:
				currentTime = time.time()
				duration = currentTime - startTime
				print "[", time.strftime("%H:%M:%S", time.localtime(currentTime)),"]",
				print "[", time.strftime("%H:%M:%S", time.gmtime(duration)),"]",
				print "%i and %i are in love!" % (n, m)
	else:
		break

currentTime = time.time()
duration = currentTime - startTime
print "End Time:",time.strftime("%H:%M:%S", time.localtime(startTime))
print "Time Elapsed:", time.strftime("%H:%M:%S", time.gmtime(duration))