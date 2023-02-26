def find_factor(n):
    if n==1:
        return 1
    
    return n*find_factor(n-1)

print(find_factor(3))



#find power

def findpower(x,n):
    if n==0:
        return 1
    else:
        return x*findpower(x,n-1)
    

print(f"power is {findpower(3,2)} ")


#find gcd

import numpy as np

mygcd = np.gcd.reduce(np.array([90,20,30,40]))
print(mygcd)
