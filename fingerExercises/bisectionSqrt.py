#! /usr/bin/python3 
# Implements bisection search to find the square root of a number x 

x = 0 
while x <= 0:
    x = int(input('Find the square root of:'))
    
epsilon = 0.00001
low = 0 
high = max(1.0, x) 
guess = (high + low)/2
numGuesses = 1 

while abs(guess**2 - x) >= epsilon:
    if guess**2 > x:
        high = guess 
    else: 
        low = guess 
    guess = (high + low)/2
    numGuesses += 1

print("The square root of {} is approximately {}".format(x, guess))     
print("Number of guesses took: {}".format(numGuesses))       