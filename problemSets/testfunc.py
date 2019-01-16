# /usr/bin/python3 
# testfunc.py : program contains a function testfunc that takes in a function and a list 
# as parameters and prints out the result of implementing the function for each element

# function is used for testing other functions w a test suite 

def testfunc(f, L1):
    for elem in L1:
        result = f(elem)
        print("Passing {} into function gives {}".format(elem, result))

        