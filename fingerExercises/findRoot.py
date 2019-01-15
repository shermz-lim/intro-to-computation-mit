# Implements bisection search to find the x root of a number 


def findRoot(num, power, epsilon):
    """Assumes num and epsilon int or float, power an int,
        epsilon > 0 & power >= 1
        Returns float y such that y**power is within epsilon of num.
        If such a float does not exist, it returns None"""
    
    if power % 2 == 0 and num < 0:
        return 
        
    low = min(-1.0, num)
    high = max(1.0, num) 
    guess = (high + low)/2

    while abs(guess**power - num) >= epsilon:
        if guess**power > num:
            high = guess 
        else: 
            low = guess
   
        guess = (high + low)/2.0

    return guess    

def testFindRoot():
    epsilon = 0.000001
    for num in (-0.25, 0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            result = findRoot(num, power, epsilon)
            if result == None:
                print("{} has no {}th root.".format(num, power))
            else:
                print("{}**{} ~= {}".format(result, power, num))

testFindRoot()                    