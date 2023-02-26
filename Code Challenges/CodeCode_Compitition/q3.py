"""generate sequences of (sequences of 0's and 1's ) of length 19 are there that begin with a 0, end with a 0,
contain no two consecutive 0's and contan no three consecutive 1's"""

import random
import math as m

n=19
global my_array
my_array=[]

def my_fun(n):
    for i in range(n+1):
        if i==0 or i==n-1:
            my_array.append(0)
            continue

        if i==1 or i==n-1:
            my_array.append(1)
            continue
    
        if my_array[i-1]==0:
            my_array.append(1)
            continue
        
        if my_array[i-1]==1:
            if(my_array[i-2]==1):
                my_array.append(0)
                continue
        
        
        # find random number between 0 and 1
        random_number= random.randint(0,1)
        my_array.append(random_number)
    
    return my_array


print(array_of_array)

        

