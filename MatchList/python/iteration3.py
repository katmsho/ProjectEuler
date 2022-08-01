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
from math import floor
import sys
from xmlrpc.client import Boolean

#need to return found, is less than center, key is greater than center, key no match (length = 1)
def findKey(item, b) -> Boolean:
 
    dictLength = len(b)
    dictCenter = floor(dictLength/2)
    dictCenterKeyName = list(b.keys())[dictCenter]
    itemKey = item[0]
    itemValue = item[1]
    if itemKey == dictCenterKeyName and (type(itemValue)==type(b[dictCenterKeyName])):
        if (type(itemValue) is dict): 
            return findKeys(itemValue,b[dictCenterKeyName])
        return True  #found
    if itemKey != dictCenterKeyName and dictLength==1:
        return False #not found
    if itemKey < dictCenterKeyName:    
        return findKey(item, dict(list(b.items())[:dictCenter]))
    if itemKey > dictCenterKeyName:
        return findKey(item, dict(list(b.items())[dictCenter+1:]))

def findKeys(a,b) -> Boolean:
    
    for item in a.items():
        result = findKey(item,b)
        if not result:
            print ("Key " + item[0] + " not in B")
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