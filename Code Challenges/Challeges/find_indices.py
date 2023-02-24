#MY Codes 

import numpy as np

myinput = np.array(input().split())

target = int(input("Enter the target sum = "))


def myfun(target,myinput):
    size = len(myinput)
    for j in range (0,size-1):
        for i in range (j+1,size):
            if(target == int(myinput[j])+int(myinput[i])):
                return (np.array([j,i]).tolist())

result = myfun(target,myinput)
print("The array index are = {}".format(result))


# Another optimized code :


import numpy as np

myinput = np.array(input().split())

target = int(input("Enter the target sum = "))


def myfun(target,myinput):
    size = len(myinput)

    for j in range (0,size-1):
        my_index = target - myinput[j]
        if my_index in myinput:
            index = np.where(myinput==my_index)[0]

        return (np.array([j,input]).tolist())
result = myfun(target,myinput)
print("The array index are = {}".format(result))