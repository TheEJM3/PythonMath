#Coded by TheEJM3 on 3/2/2017
#YouTube Username: The EJM3
#YouTube Channel: https://www.youtube.com/channel/UCiv7jEOluBBXM3ystrNlRJw
#Reddit:  /u/TheEJM3

#This code was written for the March 2017 Lockpicking Advent Calendar.
#The goal of the calendar is to promote Locksport, grow the community and...
#HAVE FUN!

#All the rules and information can be found in our announcement video found here:
# https://youtu.be/MLJwE5Sg4CE

#The output of this code will randomize a pinning for a 6 chamber practice lock.
#Please check the notes next to the code to customize the code for your lock / pins


from random import randint 

print " "
print " "

print "Random Chamber Pinning for the"
print "Lockpicking Advent Calendar, March 2017"
print "Coded by TheEJM3"
print "https://www.youtube.com/channel/UCiv7jEOluBBXM3ystrNlRJw"

print " "

i = 1

while i <= 6: #Replace "6" with the number of chambers in your lock.
	
	p = randint(1,4) #Replace 4 with the amount of different types of pins you have available.
	s = randint(1,2) #Replace 2 with the amount of different types of springs you have available.
	
	if p == 1: #Will change randomly-generated number to a type of pin.  "1" turns into...
		pin = 'standard' #"standard".  Replace standard with any type of pin
	if p == 2: #This repeats the pattern seen in the previous 2 lines - "2" will be...
		pin = 'spool' #a spool pin.
	if p == 3: #There are four options for pin types. If you entered "3" in the line 
		pin = 'mushroom' #"p = randint(1,3)", then delete the next two lines of code because
	if p == 4: #"p" will never equal 4. If you entered "5" in the "p = randint(1,5)" line
		pin = 'serrated' #then insert two lines of code and follow the same pattern for the first 4
	
	if s == 1: #These next four lines are similar to pattern above, but this time we are 
		spring = 'copper' #entering the different types of springs.  1 = copper, 2 = steel
	if s == 2: #Add or remove lines of code to match the "s = randint(1,x)" line
		spring = 'steel'
		
	#The next line of code is a bit tricky, but I'll explain.  This will output the randomly-generated
	#pin and spring combination for each chamber.  We are inside of a "while loop" that will repeat
	#as many times as the amount we entered as "x" in the line of code above "while i <= x:"
	#In the original version of the code, I want 6 randomly-generated pin and spring combinations with
	#the output saying "Chamber 1: Use a serrated pin with a copper spring", for example.  
	
	#Study the next line a code for a moment and try to comprehend what you just read.
	
	#We are using 3 variables: the first is the chamber number, the second is the pin type and the 
	#third is the spring type.  For each of these variables, we can enter a "%" symbol and a "d" or an 
	#"s".  The "d" and "s" are the type of variable, "d" for decimal, "s" for string. I used the "%d" 
	#after the word "Chamber" to indicate that a variable in decimal form will be going there.  
	
	#After the word "spring"", there is another "%".  This tells python that I will be listing the 
	#variables that I would like to replace the "%"s with in the same order as they appear.  The 
	#variable "i" will replace the "%d". The first time around the "i" will be a "1" because we wrote 
	#"i = 1" at the top of the code.  "i" will count up by 1 each time we go around this loop because 
	#of the last line of code: "i = i + 1", which in plain English reads, "The new value of "i" will 
	#be the old value of i plus 1." So the next time we go around the loop, "i" will be 2.  
	
	#The loop stops when try to go around a 7th time. "i"'s value is 7 on the seventh time around the
	#loop and will be stopped by the line "while i <= 6" because this statement is no longer true: 
	#7 is not less than or equal to 6.  
	
	#At this point, the program will continue with the first line of code following this loop.  Because
	#there are no additional lines after the loop, the code stops.
	
	#The other two "%"s are the pin and spring variables we randomly created above.  Because we put
	#the randomization code for the pin & spring in the loop section, they will generate a new pin
	#and spring combination each time the program loops.

	
	print "Chamber %d: Use a %s pin with a %s spring" % (
		i, pin, spring)
		
	#If you want to add a third challenge option, for example to vary the key pin type (standard or 
	#serrated), then a fourth variable can be added below the "if s == 1" section.  We can use "k" as 
	#our randomly-generated number and "key" when replace the random number with the string "standard" 
	#or "serrated". Copy and paste the "if s == 1" section, replace the "s"s with "k"s, the "springs" 
	#with "key", and "'copper'" and "'steel'" with "'standard'" and "'serrated'".  The previous lines 
	#could be replaced with this, for example:
	
	#print "Chamber %d: Use a %s driver pin with a %s key pin and a %s spring" % (
	#	i, pin, key, spring)
	
	#If you want to customize the code, please try to figure this out and give it a try before you 
	#preemptively ask for help.  The best way to learn is by first understanding how this works by
	#reading these notes, then synthesizing what you have learned to create something new.  If you
	#are really stuck, then by all means leave a comment on the YouTube video where I post this 
	#here:
	
	#Here's the catch:  I will only answer questions in the following format:  The first line of your
	#comment needs to be "TheEJM3," and a flattering comment about my channel or video. Subscribing
	#would be awesome too. Secondly, you need to insert your favorite number, animal, lock, color, 
	#lockpick, toothpaste, and YouTube locksport channel besides BosnianBill, randomly throughout 
	#your question.  You do not need it to make sense.  In fact, the more reads like tourettes, 
	#the better / funnier it will be. All other requests will be guided back to these notes until 
	#they give this a whirl.
	
	i = i + 1 #counts up by 1 then goes to the top of the loop: the line "while i <= 6:"
	
	#Thank you all for joining in with the Lockpicking Advent Calendar 2017.  I hope you are all 
	#having as much fun as I am making this content and challenging myself to advance my skills.
	
	#Until next time, 
	
	#Peace
	
	#-TheEJM3
