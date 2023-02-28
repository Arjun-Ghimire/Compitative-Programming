"""Find the sum of all numbers less than 2000 that are divisible by 13 but not by 19"""

def sum_of_divisors(n):
    mysum = 0
    for i in range(0, n):
        if i % 13 == 0 and i%19!=0:
            mysum += i
    return mysum



print(f"The sum is = {sum_of_divisors(2000)}")