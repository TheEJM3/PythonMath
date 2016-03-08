This is a collection of Python scripts to calculate integer sequences
and other fun number stuff.

Fib.py simply compiles the Fibinacci sequence from 1 to what ever number is
entered, then divides the last number in the sequence by the previous number
in the sequence. Mathematicians cliam that the product tends to Phi, the
Golden Radio, but, well, have a go with the script and see what happens.

AmicableBruteForce.py finds amicable pairs. An amicable pair is one whos factors
match the other number in the pair.  For example, 220 has the factors 1, 2, 4,
5, 10, 11, 20, 22, 44, 55, and 110 which all add up to 284.  284 has the 
factors 1, 2, 4, 71, and 142 which add up to 220.  These 2 numbers are meant
to be together.  They are in love.  Historically, lovers carved these numbers
into opposite sides of fruit then both eat half.  It is said that when the
fruit is consumed, the lovers become complete.
AmicableBruteForce.py calculates the factors of an input, adds them up, then
does the same thing with the sum.  If the second sum matches the input number
then the pair is amicable.

ChristaNumbers.py uses the proof from this paper:
https://www.maa.org/sites/default/files/pdf/upload_library/22/Evans/pp.05-07.pdf
The paper takes Euler's proof and simplifies it to four steps:
1) a = pick a number, any number
2) a/((2a)-o(a)) yeilds b/c which then is reduced from to its simplest form
3) find all possible x and y for (cx-b)(cy-b)=b^2
4) if p=x-1, q=y-1, and r=xy-1 are all primes, then M=apq and N=ar are
canidates for an amicable pair.
I read that Euler's proof only gave two, known false positives, but this
proof gives more.  I'm not sure if the paper is correct.  More to come on this.

ExpOfTwo.py calculates the exponets of 2 from 2^0 to 2^x where x is defined by 
the user. My coworker told me about a game his and his son play in the car.  
They take 1 then double it, and double it, and double it, etc... until they 
can't compute the next one in their head.  I wrote this code mostly to show 
him how this calculation could be done in Python.  He pointed out that their 
record is 2^25.  Not bad, Justin.  Not bad at all.

FactorsOfSquare.py is a simple code that prints all factors of a number squared. 
I wrote this one as a prototype for the ChristaNumbers.py script.  It might be 
helpful for someone else that needs a script like this, but a more universal 
function was ultimately written for use in the ChristaNumbers.py script.