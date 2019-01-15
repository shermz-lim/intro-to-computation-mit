#! python3 
# Implements the Newton Raphson approximation algorithm to finding the sqrt of a number

k = -1
while k < 0: 
    k = float(input("Find the square root of: "))

epsilon = 0.001
guess = k/2   #1st guess 
numGuesses = 1

# polynomial: guess**2 - k = 0 . Derivative of polynomial: 2 * guess 
while abs(guess**2 - k) >= epsilon:
    guess = guess - (guess**2 - k)/(2 * guess)
    numGuesses += 1

print("Square root of {} is about {}. Number of guesses: {}".format(k, guess, numGuesses))    