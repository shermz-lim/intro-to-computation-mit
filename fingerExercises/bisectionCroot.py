#! /usr/bin/python3 
# Implements bisection search to find the cube root of a number x 
# Have to take into account -ve numbers 

x = float(input('Find the cube root of:'))

epsilon = 0.00001

low = min(-1.0, x)
high = max(1.0, x) 
guess = (high + low)/2
numGuesses = 0 

while abs(guess**3 - x) >= epsilon:
    if guess**3 > x:
        high = guess 
    else: 
        low = guess
    numGuesses += 1      
    guess = (high + low)/2


print("The cube root of {} is approximately {}".format(x, guess))            
print("Number of guesses took: {}".format(numGuesses))