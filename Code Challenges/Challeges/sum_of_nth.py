# Sum of nth natural numbers 

def sum_nth(n):
    if n==1:
        return 1
    
    return n + sum_nth(n-1)


print(f"The sum of 15 is {sum_nth(15)}")
