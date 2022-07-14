"""
Implementation of https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Re-learning python after many years, and intro to v3

Bit of a refactor & making generic. Just because

>>> main(1000, [3,5])
233168.0
"""


from decimal import DivisionByZero
import sys
from timeit import default_timer as timer

def main(dividend,divisors):
    """
    Program takes two integer arguments and finds the sum of the multiples of sys.argv[2] the occur below sys.argv[1]

    :param dividend:  integer the multiples of divisors must be less than
    :param divisors:  comma separated list of two integers.   
    """
  
    total=0
    for divisor in divisors:
       highestDivisbleNumber =  ((dividend-1) // divisor) * divisor
       total += getNumbers(highestDivisbleNumber,divisor)
    
    # This works when you are submitting 2 numbers
    # if submitting > 2 then this deletes too much, as numbers can be replicated
    #TODO - need to think about cases when we are removing number multiple times, how to absrtract switch between adding/removing sums
    numList=[divisors[0]*divisors[1]]
    for number in numList:
        highestDivisbleNumber =  ((dividend-1) // number) * number
        total -= getNumbers(highestDivisbleNumber,number) 
    print (total)


#print(getNumbers(((999 // 3)*3),3) + getNumbers(((999 // 5)*5), 5) - getNumbers(((999 // 15)*15), 15) )
def getNumbers(dividend, divisor):
    return divisor * (dividend/divisor) * ((dividend/divisor)+1) / 2
  
def getDividend():
    try:
        return int(sys.argv[1])
    except ValueError:
        print ("dividend must be integers")
        exit()

def getDivisors():
    try:
        divisors = sys.argv[2].split(",")
        return list(map(int, divisors))
    except ValueError:
        print ("all divisors must be integers")
        exit()

def checkInput(dividend,divisors):
    if len(sys.argv)!=3:
        print ("expected only dividend and divisors list as arguments")
        exit()

    if len(divisors)!=2:
        print ("expected two integers in divisors list")
        exit()

if __name__ == "__main__":
    if sys.argv[1]=='--help':
        print(__doc__)
        exit()

    if sys.argv[1]=='--test':
        import doctest
        doctest.testmod()
        exit()

    if len(sys.argv)!=3:
        print ("expected dividend and divisors list as arguments")
        exit()

    dividend=getDividend()
    divisors=getDivisors()
    checkInput(dividend,divisors)

    start = timer()
    main(dividend, divisors)
    end = timer()
    print("Elapsed time: " + str(end - start) + " seconds") 