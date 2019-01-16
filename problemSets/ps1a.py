# /usr/bin/python3
# solution to pset 1a - House Hunting 

# Obtaining initial variables from user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to be saved in decimal form (0.01 to 0.99): "))
total_cost = float(input("Enter the cost of your dream home: "))

assert (portion_saved > 0 and portion_saved < 1)
assert total_cost > 0
assert annual_salary > 0

# Initialize variables  
portion_down_payment = 0.25 
current_savings = 0 
r = 0.04
numMonths = 0 

# every month current_savings become previous current + previous current x 0.04 + monthly
# Caclulating variables 
monthly_salary = annual_salary/12 
monthly_savings = monthly_salary * portion_saved
down_payment = 0.25 * total_cost

while current_savings < down_payment:
    # Incrementing current savings with increase for a month from salary & investment
    numMonths += 1 
    current_savings = current_savings*r/12 + current_savings + monthly_savings

print("Number of months: " + str(numMonths))

    