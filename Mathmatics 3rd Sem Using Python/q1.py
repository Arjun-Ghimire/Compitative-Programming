# Check consistency of the equations 5x+3y +7z=4, 3x+26y+2z=9, 7x+2y+10z = 5.
#if it is consistence find its solution.

# consistency means that it has one equation that satisfies all the equation in the system

import numpy as np

A = np.array([[5,3,7],[3,26,2],[7,2,10]])
B = np.array([4,9,5])

detA = np.linalg.det(A)

# If the determinant is non-zero, the system is consistent and has a unique solution
if detA!=0:
    print(" It is consistent ")

else:
    print("It is not consistent")