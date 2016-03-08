#OneRollYahtzee counts the amount of rolls it takes to
#make a one roll Yahtzee.

import random

def roll_dice():
	die0 = random.randrange(1,7,1)
	die1 = random.randrange(1,7,1)
	die2 = random.randrange(1,7,1)
	die3 = random.randrange(1,7,1)
	die4 = random.randrange(1,7,1)

	roll = [die0,die1,die2,die3,die4]

	return roll

def check_yahtzee(a,b,c,d,e):
	if a == b:
		if b == c:
			if c == d:
				if d == e:
					return True

count = 1
yahtzeeCount = input("Enter amount of 1 roll Yahtzees: ")

for x in xrange(1, yahtzeeCount+1):
	a,b,c,d,e = roll_dice()
	yahtzee = check_yahtzee(a,b,c,d,e)
	while yahtzee != True:
		count = count + 1
		a,b,c,d,e = roll_dice()
		print a, b, c, d, e
		yahtzee = check_yahtzee(a,b,c,d,e)
	print count
	
print "%i Yahtzees only took %i rolls" % (yahtzeeCount, count)

average = (count/yahtzeeCount)

print "It took an average of %i rolls per Yahtzee" % average