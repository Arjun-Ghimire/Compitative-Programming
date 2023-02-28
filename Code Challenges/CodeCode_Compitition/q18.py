""" What is the sum of all integers  n such that 
n(square) + 2n + 2 divides n(cube) + 4n(square) + 4n - 14 ? 
Write an answer in its absolute form. """

import math as m
global sum

def sum_of_eqn(n):
    mysum = 0
    for i in range(1,n):
        eqn1 = m.pow(i,2) + 2*i +2
        eqn2 = m.pow(i,3) + 4*pow(i,2) +4*i -14

        if eqn2%eqn1 == 0:
            mysum += i
    return mysum

print(abs(sum_of_eqn(10000000))) 