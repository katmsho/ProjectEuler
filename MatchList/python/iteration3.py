"""
Re-learning python after many years, and intro to v3
Deliberately naive & simple coding to be obvious & provide correct answer to validate later implementations

Find if dict b has the same keys as dict a  (e.g. for API response, can add extra items but not remove)
Value must now be the same type
Adding sub-dictionary
Allow for large data sets: Assume dicts are sorted, so can use binary search to find key

Testing via CLI: python .\iteration3.py --test
>>> main({"a":1, "b":"2"},{"a":1, "b":"2", "c":"three"})
All keys in A found in B

>>> main({"a":1, "b":"2", "d":4},{"a":1, "b":"2", "c":"three"})
Key d not in B

#>>> main({"a":1, "b":"2"},{"a":1, "b":2, "c":"three"})
#Key b not in B

>>> main({"a":1, "b":"2", "d":{"e":"e"}},{"a":1, "b":"2", "c":"three"})
Key d not in B


"""
from math import floor
import sys
from xmlrpc.client import Boolean

#need to return found, is less than center, key is greater than center, key no match (length = 1)
def findKey(key, b) -> Boolean:
    dictLength = len(b)
    dictCenter = floor(dictLength/2)
    dictCenterKeyName = list(b.keys())[dictCenter]
    if key == dictCenterKeyName:
        return True  #found
    if key != dictCenterKeyName and dictLength==1:
        return False #not found
    if key < dictCenterKeyName:    
        return findKey(key, dict(list(b.items())[:dictCenter]))
    if key > dictCenterKeyName:
        return findKey(key, dict(list(b.items())[dictCenter+1:]))

def findKeys(a,b) -> Boolean:
    for keyA in a.keys():
        result = findKey(keyA,b)
        if not result:
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