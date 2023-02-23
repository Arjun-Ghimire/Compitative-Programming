# Write a program that computes the determinant of a square matrix using Gaussian elimination.

import numpy as n;

myarray = n.array([[10,20,30],[40,50,70],[20,30,22]])

mydeterminant = n.linalg.det(myarray)

print(mydeterminant)