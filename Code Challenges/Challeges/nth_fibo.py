# Implement a program that calculates the nth Fibonacci number using dynamic programming.


def findfibo(n):
    if n==0:
        return 0
    
    elif n==1:
        return 1
    
    elif n>=2:
        return findfibo(n-1)+findfibo(n-2)


x = int(input())

print("The fibo sum is = {}".format(findfibo(x)))