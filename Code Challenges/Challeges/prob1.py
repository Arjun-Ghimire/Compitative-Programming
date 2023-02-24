""" Count numbers from 10 to 4000 whose:
a) Number of divisors is even

b) Sum of all divisors is prime. """
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(10, 4001):
    divisors = 0
    divisor_sum = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisors += 1
            divisor_sum += j
            if j != i // j:
                divisors += 1
                divisor_sum += i // j
    if divisors % 2 == 0 and is_prime(divisor_sum):
        count += 1

print("The number of such numbers is:", count)
