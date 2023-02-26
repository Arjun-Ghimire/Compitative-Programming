""" We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime. What is the largest n-digit pandigital prime that
 exists? """

import itertools as it
import math as m

#since pandigital max n can be 9 so that :
n = 9

global num_array # this is used to store number arrays 1 to n for each value of n
global prime_numbers 

# two arrays to hold prime numbers and numbers
num_array = []
prime_numbers=[]

def pandigital_max(num):

    # for each value of n from 1 to 9
    for n in range(1,num+1):
        
        # everytime we empty this so that it will store value from 1 to n interation
        num_array = []

        #storing the value to the num array
        for i in range(1,n+1):
            num_array.append(i)

        # this will generate all the possible permutation array and store it to the num_array2
        num_array2 = list(it.permutations(num_array))
        array_len= len(num_array2)
        
        # this will check till array_len
        for i in range(array_len):

            # this will join the [1,2,3,5] etc values into 12345 and store it back to num_array2
            num_array2[i] = ''.join(map(str,num_array2[i]))

            # this will check if num_array2[i] is prime or not
            if(is_prime(num_array2[i])):

                # storing all the values to the array so that we can takeout make from this
                prime_numbers.append(num_array2[i])


def is_prime(n):
    n = int(n)
    if n<=2:
        return False
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(m.sqrt(n))+1):
        if n%i==0 or n%(i+2)==0:
            return False
        
    return True


# find permutation from numpy array
pandigital_max(n)

# displaying the max values from the prime_numbers array
print("The maximum prime and pandigital number is = {} ".format(max(prime_numbers)))
