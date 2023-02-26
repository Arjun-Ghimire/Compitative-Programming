""" We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime. What is the largest n-digit pandigital prime that
 exists? """



import math as m

n = 9 #this means 4 digit pandigital number
global prime_array
prime_array = []
global myarray
myarray = []

def check_greater(n):
    status = True
    for i in str(n):
        if i>0 and i<5:
            status = False
    
    return status


def is_pandigital(n):
    
    max = 0 #since the number more then 4321 cannot be pandigital number
    min = 999999999 #since the number less then 1234 cannot be pandigital number

    for i in range(min,max+1):
        my_string = set(str(i)) #this will make the unique set of my_string
        my_int = int(str(my_string))
        if any(0 < num < 5 for num in my_int):

            if len(my_string)==4: #this means that the length is 4
                if(is_prime(i)):
                    prime_array.append(i)

# Checking prime number here
def is_prime(n):
    if n<=2:
        return False
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(m.sqrt(n))+1):
        if n%i==0 or n%(i+2)==0:
            return False
        
    return True


is_pandigital(n)

print("The is maximum prime number of pandigital of 4 digits is = {}".format(max(prime_array)))



# My message =

""" LOL I Spend few hours to understand this problem and knew that we solve this using the technique of permutation to find the no. of ways it can be arranged """
