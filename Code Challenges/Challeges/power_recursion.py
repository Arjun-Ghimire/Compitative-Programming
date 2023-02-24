
def power_find(x,n):
    if n==0:
        return 1

    return power_find(x,n-1)*x


print(f"The power of 2 cube 3 is {power_find(2,3)}")