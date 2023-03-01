# Let k be a positive integer< 50, find the greatest k if n power 7 - n  is
# divisble by k for every positive integer n

def find_greatest_value(k_max):
    for k in range(k_max - 1, 0, -1):
        flag=0
        for n in range(1, 50):
            if (n ** 7 - n) % k == 0:
                flag+=1
        if flag==49:
            return k
    return None
print(find_greatest_value(50))


# Another way

def find_greatest_value(k_max):
    for k in range(k_max - 1, 0, -1):
        
        for n in range(1, 50):
            if (n ** 7 - n) % k != 0:
                break
        else:
            return k
    return None
print(find_greatest_value(50))
