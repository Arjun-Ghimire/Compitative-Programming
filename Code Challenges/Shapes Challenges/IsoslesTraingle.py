
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
