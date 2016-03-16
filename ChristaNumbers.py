#Amicable Numbers Generator using Euler's method

#Edward J. McLean III
#March 5th, 2016
#Raymond, NH

#For Christa

#Given a range of numbers, this script checks to see if the current number,
# 'a' (CLP in the script),yeilds an amicable pair.  This script was
#written from this article:
#https://www.maa.org/sites/default/files/pdf/upload_library/22/Evans/pp.05-07.pdf
#In the article, Willian Dunham explains that when a number, a, is picked,
#a is then applied to the following equation: a/(2a)-o(a) where o(a) is
#the sum of all a's factors including a.  Once the equation spits out a
#fraction, the fraction is reduced to its simplest form.  b = to the
#numerator. c = to the demoninator. Then x and y needs to be worked out
#for all posible answers for: #(cx-b)(cy-b)=b^2.  Once an x y pair have
#been extracted, then p, q and r can be calculated as follows:
#p=x-1, q=y-1, and r=xy-1.  If p, q, and r are all prime numbers,
#then M and N are canidates for amicability.  M=apq and N=ar.
#There are false positives using this method, which is why I added a
#brute-force amicability checker at the very end.  The checker, called
#the "love_test", simply finds the sum of factors for M and checks if
#the sum = N.  If it does then it finds the sum of factors for N and
#checks if the sum = M.  If it does, well, the numbers were meant to
#be together forever.

#Enjoy!


import math
import time
import csv
import itertools
from fractions import Fraction

#Sums all factors of n
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

#function returns amicable pairs
def love_test(n,m):
	if factor_sum(n) == n + m:
		return True

#standard prime number checker
#copied from stackoverflow.com user "dawg" in this post: 
#http://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
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

print "Amicable Numbers - Euler Style"
print "Writen by TheEJM3 with Christa in mind. <3"

#starting number of a
min = input('Enter Min Iterations: ')
#ending number of a
max = input('Enter Max Iterations: ')
#gives updates at inputed iterations
iterations = input('Enter Update Rate: ')

#counter of a, will add the 1 back @ line 118
count = min - 1
#grabs the int divide for multiplier and modulo for count
multiplier, count = divmod(count, iterations)
#for multiplication @ line 126, will be 5k off otherwise
multiplier = multiplier + 1
#grabs the start time
startTime = time.time()
#prints start time
print "Start Time:",time.strftime("%H:%M:%S", time.localtime(startTime))

#opens the .csv file and writes the header
with open('AmicablePairs.csv', 'ab') as datafile:
	csv_writer = csv.writer(datafile, delimiter=',')
	data = ["Time Elap","a =", "M =", "N =",]
	csv_writer.writerow(data)

#main function
for CLP in itertools.count(min):
	if CLP < max + 1:
	
	#starts counting the iterations
		count = count + 1

		#every x # of iterations it records the time and where it's at
		if count == iterations:
			currentTime = time.time()
			duration = currentTime - startTime
			print "[",time.strftime("%H:%M:%S", time.localtime(currentTime)), "]",
			print "[",time.strftime("%H:%M:%S", time.gmtime(duration)), "]",
			print "Iteration", '{:,}'.format(int(iterations * multiplier))
			count = 0
			multiplier = multiplier + 1

		#calculates the sum of factors of current iteration
		o = factor_sum(CLP)

		#if iteration is not a perfect number...
		if (2 * CLP - o) != 0:

			#finds the simplest form of b/c
			Step2 = Fraction(int(CLP), int((2*CLP - o)))

			#b = the numerator
			b = Step2.numerator
			#c = the demoninator
			c = Step2.denominator

			#squares b
			square = b**2

			#this is where the magic happens...
			#we are trying to get the values of x and y in (cx-b)(cy-b)=b^2
			for n in itertools.count(1):
				if n < b + 1:
					#from 1 to the square root, z = b^2/n
					z = square/float(n)
					#if z is an integer, then we have a value for (cx-b) and (cy-b)
					if (z).is_integer():
						#find x in (cx-b)
						x = (z + b) / c
						#x must be an integer or else it won't work
						if (x).is_integer():
							#find y in (cy-b)
							y = (float(n) + b) / c
							#y must be an integer or else it won't work
							if (y).is_integer():
								#Prime check time! p=x-1, q=y-1 and
								#r=xy-1 all must be primes
								p = x - 1
								if is_prime(p):
									q = y - 1
									if is_prime(q):
										r = (x*y) - 1
										#if they are all primes, then M=apq and
										#N=ar are canidates for amicability
										if is_prime(r):
											M = CLP * p * q
											N = CLP * r
											#check M and N using the brute-force method in love_test
											if love_test(int(N), int(M)):
												#if they are lovers, print the numbers, time,
												#and a value on screen and in file
												currentTime = time.time()
												duration = currentTime - startTime
												print "[", time.strftime("%H:%M:%S", time.localtime(currentTime)),"]",
												print "[", time.strftime("%H:%M:%S", time.gmtime(duration)),"]",
												print '{:,}'.format(int(M)),"and", '{:,}'.format(int(N)),
												print "are in love!  a = ", '{:,}'.format(int(CLP))
												with open('AmicablePairs.csv', 'ab') as datafile:
													csv_writer = csv.writer(datafile, delimiter=',')
													data = [time.strftime("%H:%M:%S", time.gmtime(duration)),CLP, M, N,]
													csv_writer.writerow(data)
				else:
					break
	else:
		break