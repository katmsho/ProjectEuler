"""
Implementation of https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Re-learning python after many years, and intro to v3

Bit of a refactor & making generic. Just because

"""

import sys
from timeit import default_timer as timer

def main():
    if len(sys.argv)==2 and sys.argv[1]=='--help':
        print(__doc__)
        exit()

    start = timer()

    dividend = int(sys.argv[1])
    divisors = sys.argv[2].split(",")
    numList=[]

    for divisor in divisors:
        numList=list(set(numList + getNumbers(dividend,int(divisor))))
 
    print(sum(numList))

    end = timer()
    print("Elapsed time: " + str(end - start) + " seconds") 
    

def getNumbers(dividend, divisor):
    """ 
    remove 1 from dividend, and add it back in when doing for...range
    this is necessary as range is not inclusive and so we need to add 1 to it to make sure we get a list of all multiples of divisor
    however, if a divisor goes into dividend exactly we do not want the extra as the requirement of the problem is for all multiples below dividend
    therefore we remove 1 from the starting dividend
    e.g. multiples of 3,5 below 1000
    multiples of 3: 3...999
    multiples of 5: 5...995  (1000 should not be included)
    """
    quotient = (dividend-1) // divisor

    numList=[]

    for i in range(1, quotient+1):
        numList.append(i*divisor)
   
    return numList

if __name__ == "__main__":
    main()