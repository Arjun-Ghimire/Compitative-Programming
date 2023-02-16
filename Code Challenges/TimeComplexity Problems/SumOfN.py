# Time complexity problems


def sum1(n):
    # Here the time complexity is O(1) since it doens't have any loops
    return n*(n+1)//2


def sum2(n):
    sum =0
    for i in range(1,n+1):
        sum +=i
    
    return sum

# no. of test cases
total = int(input())

while total :
    mynum = int(input())
    
    print("The sum of nth number from 1st function is = "+ str(sum1(mynum)))
    print("The sum of nth number from 2nd function is = "+ str(sum2(mynum)))

    total=total-1
    
