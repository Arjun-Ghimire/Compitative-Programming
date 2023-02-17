# here I will be finding the divisible terms with the different time complexity of O(n) and O(root n)

from math import *

def divisible_term(num):
    div1 = []
    for i in range(1,num+1):
        if(num%i==0):
            div1.append(i)

    return div1
    
def divisible_term2(num):
    div2 = set()
    for i in range(1,int(sqrt(num)+1)):
        if(num%i==0):
            div2.add(i)
            div2.add(num//i)
        

    return list(div2)
    


number = int(input())

# finding the divisible terms of number 

print("The divisible terms of {} are {} ".format(number,divisible_term(number)))
print("From second way, The divisible terms of {} are {} ".format(number,divisible_term2(number)))
