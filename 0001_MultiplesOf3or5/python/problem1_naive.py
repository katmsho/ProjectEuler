"""
Implementation of https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Re-learning python after many years, and intro to v3
Deliberately naive & simple coding to be obvious & provide correct answer to validate later implementations
"""
from timeit import default_timer as timer

def main():
    start = timer()
    numList=[]
    
    for i in range(1,1000):
       
        if i%3 == 0:
            numList.append(i)
            
        elif i%5 == 0:
            numList.append(i)
            
    sum=0

    for i in range(0,len(numList)):
        sum = sum + numList[i]

    print(sum)

    end = timer()
    print("Elapsed time: " + str(end - start) + " seconds") 

if __name__ == "__main__":
    main()