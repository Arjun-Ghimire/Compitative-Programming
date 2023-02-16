
"""
showing this shape = 

         *  
       *   *  
     *   *   *  
   *   *   *   *  
 *   *   *   *   *  

"""

for x in range (5):
    for z in range (4-x):
        print("",end=" ")
    
    for y in range (x+1):
        print("*",end=" ")
    
    print()

"""
showing this shape = 

        * 
      * * 
    * * * 
  * * * * 
* * * * *

"""

for x in range (5):
    for z in range (4-x):
        print(" ",end=" ")
    
    for y in range (x+1):
        print("*",end=" ")
    
    print()


"""
showing this shape = 

* 
* * 
* * * 
* * * * 
* * * * * 

"""

for x in range (5):
    
    for y in range (x+1):
        print("*",end=" ")
    
    print()

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


"""

******
**  **
* * *
*  *
* * *
**  **
******

"""

# max=7
# for i in range(0,max):
#     for j in range(0,max-1):
#         if i==0 or i==max-1:
#             print("*")
        
#         elif i==1 or i==max-2:
