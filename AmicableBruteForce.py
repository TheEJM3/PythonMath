#Amicable Numbers Generator

#Edward J. McLean III
#March 5th, 2016
#Raymond, NH

#Given a range of inputs, script will calculate the sum of factors of
#the current number less the current number, then caluclate the sum of
#the factors from the first sum.  If the second sum matches the current
#number in the range, the input and the sum of the factors of the input
#are amicable.  If the input and the sum of the factors are the same,
#the number is "perfect". The final part of the prints only if the
#current number is less than the sum of its factors which stops the
#code from printing duplicates: i.e. a and b are amicable, b and a are
#amicable.  This line of code was moved to the love_test function on
#March 6th, 2016.

#Enjoy!

import time

#Sums all factors of n
def factor_sum(n):
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
	return runSum

#function returns amicable pairs
def love_test(n):
	#returns sum of factors of input
	N = factor_sum(n) - n
	#stops loop if n is not the lowest of the pair
	if N > n:
		#returns sum of factors of first sum
		M = factor_sum(N) - N
		#if second sum matches input...
		if M == n:
			#return True
			return True

#sets lower limit of range
min = input ("Enter starting number:")
#sets upper limit of range
max = input ("Enter ending number:")
startTime = time.time()

print "Start Time:",time.strftime("%H:%M:%S", time.localtime(startTime))

#Runs through each number in range
for x in range (min, max + 1):
	#if current number is in a pair
	if love_test(x):
		#caluculate other member of pair
		N = factor_sum(x) - x
		#print the lovebirds
		currentTime = time.time()
		duration = currentTime - startTime
		print "[", time.strftime("%H:%M:%S", time.localtime(currentTime)),"]",
		print "[", time.strftime("%H:%M:%S", time.gmtime(duration)),"]",
		print '{:,}'.format(int(x)),"and",
		print '{:,}'.format(int(N)), "are in love!"

currentTime = time.time()
duration = currentTime - startTime
print "End Time:",time.strftime("%H:%M:%S", time.localtime(startTime))
print "Time Elapsed:", time.strftime("%H:%M:%S", time.gmtime(duration))
