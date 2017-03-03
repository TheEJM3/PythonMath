#Coded by TheEJM3 on 3/2/2017
#YouTube Username: The EJM3
#YouTube Channel: https://www.youtube.com/channel/UCiv7jEOluBBXM3ystrNlRJw
#Reddit:  /u/TheEJM3

#This code was written for the March 2017 Lockpicking Advent Calendar.
#The goal of the calendar is to promote Locksport, grow the community and...
#HAVE FUN!

#All the rules and information can be found in our announcement video found here:
# https://youtu.be/MLJwE5Sg4CE

#The output of this code will do one of two things: either 
#1) Pick a random lock for you to pick from a list of locks you enter or,
#2) randomize a pinning for a practice lock of any number of chambers, 
#   different driver pin types (standard, spool, serrated, etc...), key pin
#   types, key bittings, and spring types.

# To use this code to pick a random lock to pick, set the "NoOfChambers" in the
# "Randomize a Practice Lock" section to "0"


from random import randint

#Random Lock

#For a random lock to pick, type the lock names between the quotations and
#the code will pick one of them.  If you only want a random lock from a 
#set of 4, only fill out four and leave the rest at "". Leave the "NoOfChambers"
#set to 0 in the "Randomize a practice lock" section below.

#You must type something between the "" of at least one of the locks below:
Lock1 = "Abus 83"
Lock2 = ""
Lock3 = ""
Lock4 = ""
Lock5 = "Master 140"
Lock6 = ""
Lock7 = "Best SFIC"
Lock8 = ""
Lock9 = ""
Lock10 = "Mul-T-Lock Interactive"


#Randomize a Practice Lock

#For a random pinning of a lock, fill in the information below:

NoOfChambers = 6 #Enter the number of chambers your practice lock has.

#If you have many keys to choose from, list them here.
#You must type something between the "" of at least one of the keys below:
Key1 = "custom-bitted"
Key2 = ""
Key3 = ""
Key4 = ""
Key5 = ""

#If you have many types of springs to choose from, list them here
#You must type something between the "" of at least one of the springs below:
SpringType1 = "copper"
SpringType2 = "steel"
SpringType3 = ""
SpringType4 = ""
SpringType5 = ""

#If you have many types of key pins to choose from, list them here
#You must type something between the "" of at least one of the key pins below:
KeyPinType1 = "regular"
KeyPinType2 = ""
KeyPinType3 = ""
KeyPinType4 = ""
KeyPinType5 = ""

#List all the types of driver pins you have to choose from here
#You must type something between the "" of at least one of the driver pins below:
DriverPinType1 = "standard"
DriverPinType2 = "spool"
DriverPinType3 = "serrated"
DriverPinType4 = "mushroom"
DriverPinType5 = ""
DriverPinType6 = ""
DriverPinType7 = ""
DriverPinType8 = ""
DriverPinType9 = ""
DriverPinType10 = ""

#The rest of the code doesn't need to be touched, but have at it if you
#want to play around.  If you want more locks to choose from, add Lock11,
#Lock12, etc... above then add them to the LockList below.  As long as 
#there is a "LockX" above and a matching "LockX" in the list below, the
#code will work everything else out.  This is a pretty simple code that 
#only deals with lists and randomization.  I'll add notations so you 
#know what's going on.

LockList = [Lock1,Lock2,Lock3,Lock4,Lock5,
	Lock6,Lock7,Lock8,Lock9,Lock10] #Makes a list from the info above
LockList = filter(bool,LockList) #Gets rid of all blanks in list
PickedLock = LockList[randint(1,len(LockList)) - 1] #Picks a random Lock from the list

#The other sections use the same methodology as the LockList code
KeyList = [Key1,Key2,Key3,Key4,Key5]
KeyList = filter(bool,KeyList)
PickedKey = KeyList[randint(1,len(KeyList)) - 1]

SpringList = [SpringType1,SpringType2,SpringType3,SpringType4,SpringType5]
SpringList = filter(bool,SpringList)

KeyPinList = [KeyPinType1,KeyPinType2,KeyPinType3,KeyPinType4,KeyPinType5]
KeyPinList = filter(bool,KeyPinList)

DriverPinList = [DriverPinType1,DriverPinType2,DriverPinType3,DriverPinType4,
	DriverPinType5,DriverPinType6,DriverPinType7,DriverPinType8,
	DriverPinType9,DriverPinType10]
DriverPinList = filter(bool,DriverPinList)

if NoOfChambers == 0: #Uses the number of chambers to figure out if you want
						#to run the Random Lock or Randomize Practice Lock code
						
#Random Lock code
	print("You'll be picking your %s") % PickedLock #Prints random lock from list
	
#Randomize Practice Lock Code
else:
	print("") #Adds spacing to output of esthetics
	print("")
	print("You'll be pinning your %s with the bitting from your %s key.") % (
		PickedLock, PickedKey)
	print("")
		
	i = 1 #"i" is a counter for the following loop.  It's value raises by 1
			#each time we reach the end of the loop. Every time we go through 
			#the loop, one chamber is populated.  The first time through the
			#loop, the 1st chamber is populated. The second time through the 
			#loop, the 2nd chamber is populated and so on until all of the
			#chambers we have are populated.
			
	while i <= NoOfChambers: #when we start the loop a 7th time and the number
								#of chambers is only 6, the code with stop running
		PickedSpring = SpringList[randint(1,len(SpringList)) - 1] #picks random spring
		PickedKeyPin = KeyPinList[randint(1,len(KeyPinList)) - 1] #picks random key pin
		PickedDriverPin = DriverPinList[randint(1,len(DriverPinList)) - 1] #picks random driver pin
		
		#All of the random picking is done at this point and we only have to
		#print the results.  For this we are using the "%" symbol to tell
		#Python that we want one of our variables written there.  The "%d"
		#means that a number value will be there.  The "%s" means that a word
		#(technically a string of characters, but whatev) will be written there.
		#after the ")" another "%" is written as well as a "(".  We are telling
		#Python that we are now going to list the variables we want in our 
		#sentence in the same order as they appear.  First, "i": the current 
		#cycle of the loop, but also the chamber number. Then the "PickedSpring",
		#followed by the "PickedKeyPin" and "PickedDriverPin".  If you are going
		#to mess around with Python code for the first time, try changing the 
		#sentence around a bit and make it call you bad names.
		
		print("Populate chamber %d with a %s spring, a %s key pin and a %s driver pin.") % (
			i,PickedSpring,PickedKeyPin,PickedDriverPin)
		i = i + 1 #In plain English, this says, "the new value of "i" is equivelent
					#to the old value of "i" plus 1.  After this line of code, 
					#Python knows that it needs to go back up to the "while i <=..."
					#line and it will test to see if it still holds true.  If you
					#only wanted one chamber populated and put "NoOfChambers = 1",
					#after this line "i" will change from 1 to 2 and go through the 
					#"while i <= to NoOfChambers" test and will fail because 2 is not
					#less than or equal to 1.  Generally, the code will move on to 
					#the next section of code beyond the while loop, but in this case, 
					#there is no next section, so the code terminates.

#Thank you all for joining in with the Lockpicking Advent Calendar 2017.  I hope you are all 
#having as much fun as I am making this content and challenging myself to advance my skills.
	
#Until next time, 
	
#Peace
	
#-TheEJM3