"""
Implementation of https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Re-learning python after many years, and intro to v3

Another refactor and adding a class

Testing via CLI: python .\problem1_iteration4.py --test
>>> main(1000, [3,5])
233168.0
"""

from numbers import Number
import sys
from timeit import default_timer as timer

class EulerProblem1:
    """
    Takes Dividend and Divisors list and calculates the sum of natural numbers below Dividend that are multiples of the Divisors
    Currently only handles exactly 2 divisors
    """
    def __init__(self, dividend, divisors) -> None:
        self.dividend = self.__verifyDividend(dividend)
        self.divisors = self.__verifyDivisors(divisors)

    def calculate(self) -> Number:
        """
        Calculates the sum of natural number below Dividend that are multiples of the Divisors
        """
        total=0
        for divisor in self.divisors:
            highestDivisbleNumber =  ((self.dividend-1) // divisor) * divisor
            total += self.__getNumbers(highestDivisbleNumber,divisor)
        
        # This works when you are submitting 2 numbers
        # if submitting > 2 then this deletes too much, as numbers can be replicated
        #TODO - need to think about cases when we are removing number multiple times, how to abstract switch between adding/removing sums
        numList=[self.divisors[0]*self.divisors[1]]
        for number in numList:
            highestDivisbleNumber =  ((self.dividend-1) // number) * number
            total -= self.__getNumbers(highestDivisbleNumber, number)
            
        return total

    def __getNumbers(self,dividend: int, divisor: int) -> Number:
        return divisor * (dividend/divisor) * ((dividend/divisor)+1) / 2

    def __verifyDividend(self,inputDividend)-> Number:
        try:
            return abs(int(inputDividend))
        except ValueError:
            print ("Dividend must be positive integer")
            exit()

    def __verifyDivisors(self,inputDivisors):
        try:
            divisors = inputDivisors.split(",")
            if len(divisors)!=2:
                print ("expected two integers in divisors list")
                exit()
            divisors=list(map(int, divisors))
            for number in divisors:
                if 0==number:
                    print ("Divisor cannot be 0: cannot divide by zero")
                    exit()

            return divisors

        except ValueError:
            print ("All divisors must be integers")
            exit()

def main(dividend,divisors):
    """
    Program takes two integer arguments and finds the sum of the multiples of sys.argv[2] that occur below sys.argv[1]

    :param dividend:  integer the multiples of divisors must be less than
    :param divisors:  comma separated list of two integers.   
    """
    euler = EulerProblem1(dividend, divisors)
    print(euler.calculate()) 


if __name__ == "__main__":
    if len(sys.argv)==0:
        print("Must have sys args")
        exit()

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

    start = timer()
    main(sys.argv[1], sys.argv[2])
    end = timer()
    print("Elapsed time: " + str(end - start) + " seconds") 