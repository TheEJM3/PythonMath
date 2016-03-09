#OneRollYahtzee counts the amount of rolls it takes to
#make a one roll Yahtzee.

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
countarray = []

for x in xrange(1, yahtzeeCount+1):
	count = 1
	a,b,c,d,e = roll_dice()
	yahtzee = check_yahtzee(a,b,c,d,e)
	while yahtzee != True:
		count = count + 1
		a,b,c,d,e = roll_dice()
		#print a, b, c, d, e
		yahtzee = check_yahtzee(a,b,c,d,e)
	countarray.append(count)
	
average = (sum(countarray)/len(countarray))
data = pd.Series(countarray)

print "%i Yahtzees took %i rolls" % (yahtzeeCount, sum(countarray))
data.describe()
plt.hist(data, bins = 10000, normed=True, cumulative=True)
plt.title("One Roll Yahtzee Counts")
plt.xlabel("# of attempt until Yahtzee")
plt.ylabel("Frequency")
plt.show()
