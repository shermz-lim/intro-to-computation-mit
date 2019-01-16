#! /usr/bin/python3
# solution to pset 1c - Finding the right amount to save away 

# Obtaining starting salary 
annual_salary = float(input("Enter the starting salary: "))

# Given variables 
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
epsilon = 100 
numMonthsAim = 36

# Calculating variables 
down_payment = total_cost * portion_down_payment
monthly_r = r/12
monthly_salary = annual_salary/12

# function calcSavings - pass in portion_saved and it will return the savings after 36 months
def calcSavings(portion_saved):
    current_savings = 0 
    monthly_savings = monthly_salary * portion_saved
    numMonths = 0
    while numMonths < 36:
        numMonths += 1 
        current_savings = current_savings + current_savings*monthly_r + monthly_savings
        if numMonths % 6 == 0:
            monthly_savings = monthly_savings + monthly_savings * semi_annual_raise
    return current_savings       

# If unable to afford down payment even by saving all the salary, exit program 
if calcSavings(1) < down_payment:
    print("It is impossible to pay the down payment in three years.")
    exit()

    
# Conducting bisection search to find the portion_saved 

high = 10000 
low = 0 
guess = (high+low)//2
numSteps = 1
savings = calcSavings(guess/10000)

while abs(down_payment - savings) >= epsilon:
    if down_payment > savings:
        low = guess
    else:
        high = guess 
    guess = (high + low)//2
    savings = calcSavings(guess/10000)        
    numSteps += 1 

print("Best savings rate: " + str(guess/10000)) 
print("Number of bisection steps: " + str(numSteps))   