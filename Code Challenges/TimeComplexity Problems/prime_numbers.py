#prime numbers to be found with the time complexity of O(1) or time complexity of O(root n)

""" One interesting property of these numbers is that they are closely related to prime numbers. 
Specifically, every prime number greater than 3 can be expressed in the form 6k +/- 1. However, 
not all numbers of the form 6k +/- 1 are prime. """

from math import * 

def primenumber(n):
    if(n==0 or n==1):
        return False
    if(n%2==0 or n%3==0):
        return False
    
# here we did loop checking from n%(i+2) because we know that prime numbers are only 6k + 1 or 6k - 1, 
# so that we have implement that formula here

    for i in range(5,int(sqrt(n)+1)):
        if(n%i==0 or n%(i+2)==0):
            return False
    
    return True

num = int(input())
print("The prime number status of {} is {}".format(num,primenumber(num)))