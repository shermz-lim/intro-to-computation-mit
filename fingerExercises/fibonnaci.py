#! python3
# Finger exercise: When the implementation of fib in Figure 4.7 is used to
# compute fib(5), how many times does it compute the value fib(2)?

numFibCalls = 0 

def fib(n):
    if n == 2:
        global numFibCalls
        numFibCalls += 1 
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return (fib(n-1) + fib(n-2))

print(fib(5))
print(numFibCalls)