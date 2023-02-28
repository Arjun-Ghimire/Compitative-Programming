# Represent -3 to the base of (-2)
base = -2

def myfun(num):
    if num ==0:
        return '0'
    
    mysum = ''
    while num!=0:
        rem = num%base
        num = num//base
        if rem<0:
            rem+=2
            num+=1

        mysum = str(rem) + mysum
    return mysum
num = -3
result = myfun(num)
print(f'{num} in base {base} is {result}')
