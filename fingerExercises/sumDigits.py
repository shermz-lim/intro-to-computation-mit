#! python3 
# Error handling exercise - implementing it for sumDigit function 

import testfunc

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""

    total = 0 
    for char in s:
        try: 
            total += int(char)
        except ValueError:
            continue

    return total         

testsuite = ['abc', 'a2b3c', '12345', '[123]avc[123]']
testfunc.testfunc(sumDigits, testsuite)
# Passed all tests 