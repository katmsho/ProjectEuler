"""
Implementation of https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Re-learning python after many years, and intro to v3

Improvements on first naive implementation, and experimenting with python-specific code
 - getting lists of multiples of 3,5 rather than iterating full 1000
 - using set() to deduplicate list much quicker than iterating & adding to new list if not already there
 - sum can take a list, nice. And quicker than iterating the list to add

"""

from timeit import default_timer as timer

def main():
    start = timer()
    numList=[]

    # get highest multiples of 3,5 below 1000
    quotient_3 = 1000//3 + 1 # +1 needed as range is not inclusive of upper bound
    quotient_5 = 1000//5     # don't want +1 here, as 200*5 = 1000 and the problem asks for all <1000

    #create lists containing all multiples of 3,5
    #can't simply add here, as need to get rid of multiples that appear in both lists e.g. 15
    for i in range(1, quotient_3):
        numList.append(i*3)

    for i in range(1, quotient_5):
        numList.append(i*5)    

    dedupedList=set(numList) 
    print(sum(dedupedList))

    end = timer()
    print("Elapsed time: " + str(end - start) + " seconds") 

if __name__ == "__main__":
    main()