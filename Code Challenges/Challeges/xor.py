def find_unique(a):
    length = len(a)
    base = a[0]
    for i in range(1, length):
        base ^= a[i]
    print(f"The not repeated number from the array is = {base}")
    
find_unique([10, 20, 30, 20, 30])