
"""
   *
  ***
 *****
*******
 *****
  ***
   *

"""

for x in range(5):
    for y in range(4-x):
        print(" ",end="")
    
    for z in range(x+1):
        print("* ",end="")

    print()


for x in range(5):
    for a in range(x+1):
        print(" ",end="")
    
    for b in range(4-x):
        print("* ",end="")
    
    print()
