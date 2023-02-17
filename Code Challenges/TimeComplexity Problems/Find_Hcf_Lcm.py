# fiding the hcf and lcm
# We need to know that product = hcf * lcm 
# The time coplexity of this is known as O(log(min(a,b)))
def hcf(a,b):
    if a==0:
        return b
    
    return hcf(b%a,a)

def lcm(a,b):
    product = a*b
    hcfValue = hcf(a,b)
    lcm = product // hcfValue

    return lcm

num1 = int(input())
num2 = int(input())

print("The lcm is {} and hcf is {}".format(hcf(num1,num2),lcm(num1,num2)))