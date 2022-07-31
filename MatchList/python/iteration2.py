"""
Re-learning python after many years, and intro to v3
Deliberately naive & simple coding to be obvious & provide correct answer to validate later implementations

Find if dict b has the same keys as dict a  (e.g. for API response, can add extra items but not remove)
Value must now be the same type
Adding sub-dictionary
For now assume order is not important

Testing via CLI: python .\iteration1.py --test
>>> main({"a":1, "b":"2"},{"a":1, "b":"2", "c":"three"})
All keys in A found in B

>>> main({"a":1, "b":"2", "d":4},{"a":1, "b":"2", "c":"three"})
Key d not in B

>>> main({"a":1, "b":"2"},{"a":1, "b":2, "c":"three"})
Key b not in B

>>> main({"a":1, "b":"2", "d":{"e":"e"}},{"a":1, "b":"2", "c":"three"})
Key d not in B

>>> main({"a":1, "b":"2", "d":{"e":"e"}},{"a":1, "b":"2", "c":"three", "d":{"e":"e"}})
All keys in A found in B

>>> main({"a":1, "b":"2", "d":{"e":"e", "f":"f"}},{"a":1, "b":"2", "c":"three", "d":{"e":"e"}})
Key f not in B
Key d not in B

>>> main({"a":1, "b":"2", "d":{"e":"e", "f":"f"}},{"a":1, "b":"2", "c":"three", "d":{"e":"e","f":1}})
Key f not in B
Key d not in B

>>> main({"a":1, "b":"2", "d":{"e":"e", "f":"f"}},{"a":1, "b":"2", "c":"three", "d":{"e":"e","f":"f"}})
All keys in A found in B
"""
import sys
from xmlrpc.client import Boolean

def findKeys(a,b) -> Boolean:
    for keyA in a.keys():
        foundKey = False
        for keyB in b.keys():
            if keyA==keyB and (type(a[keyA])==type(b[keyB])):
                if (type(a[keyA]) is dict):
                    foundKey = findKeys(a[keyA], b[keyB])
                else: 
                    foundKey=True
                break

        if foundKey==False:
            print ("Key " + keyA + " not in B")
            return False
    
    return True

def main(a,b):

    if findKeys(a,b):
        print ("All keys in A found in B")

if __name__ == "__main__":
    if sys.argv[1]=='--test':
        import doctest
        doctest.testmod()
        exit()

    main(sys.argv[1], sys.argv[2])