"""
*******
**   **
* * * *
*  *  *
* * * *
**   **
*******

"""

# set the size of the pattern
size = 7

# loop through each row of the pattern
for i in range(size):
    # loop through each column of the pattern
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1 or j == i or j == size - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
