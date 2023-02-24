
import numpy as np

array_num = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
global highest
global sum
""" def find_sum(array_num):
    highest=array_num[0]
    for i in range(0,len(array_num)-1):
            if array_num[i+1]>array_num[i]:
                    if array_num[i+1]>highest:
                            highest=array_num[i+1]

    return highest """

height_num = max(array_num)

print(f"The highest num is = {height_num}")
sum =0

for i in range (1,len(array_num)-1):
       if(array_num[i]>1 and array_num[i]<=height_num) :
              sum = sum + array_num[i]

       
print(f"The sum is is {sum}")