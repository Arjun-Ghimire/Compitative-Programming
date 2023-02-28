""" Calculating factorials for a big number is a tedious task, but finding the number of tailing zeros is slightly easier. Find the
number of trailing zeros in 1331! """

import math as m

def find_zero(n):
    total_zero =0
    if n<pow(5,5) and n>pow(5,4):
        # since it is greater then 4 and less then 5
        power_term=4

    for i in range(1,power_term+1):
        total_zero=total_zero + int(n//m.pow(5,i))
    
    return total_zero

print(f"The trailling zero are = {find_zero(1331)}")