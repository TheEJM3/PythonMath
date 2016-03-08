#Exponents of 2

#Edward J. McLean III
#March 8th, 2016
#Raymond, NH

#calculates the exponets of 2 from 2^0 to 2^x where x 
#is defined by the user. My coworker told me about a 
#game his and his son play in the car.  They take 1 
#then double it, and double it, and double it, etc... 
#until they can't compute the next one in their head.  
#I wrote this code mostly to show him how this 
#calculation could be done in Python.  He pointed
#out that their record is 2^25.  Not bad, Justin. Not
#bad at all.

#Enjoy!

currExp = 0
iteration = 0
n = input ("Enter Max Number of Exponents: ")

while (iteration < n + 1):
	currExp = 2 ** iteration
	print "2^%i = " % iteration, '{:,}'.format(currExp)
	iteration = iteration + 1

currExp = 2 ** n
print "2^%i = " % n, '{:,}'.format(currExp)