
"""
*****
*   *
*   *
*   *
*****
"""

max =5
for x in range(0,max):
    for y in range(0,max):
        if x==0 or x==max-1:
            print("*",end="")
        
        else :
            if y==0 or y==max-1:
                print("*",end="")

            else:
                print(" ",end="")

    print()
