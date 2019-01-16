#! python3
# Implement a function that satisfies the specification 

from testfunc import testfunc

def findAnEven(l):
    """Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number"""
    for elem in l:
        if elem % 2 == 0:
            return elem 

    raise ValueError('l does not contain an even number.')        

