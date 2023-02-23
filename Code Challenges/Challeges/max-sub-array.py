# find the sum of maximum of the array.

import numpy as np

def max_subarray_sum(arr):
    n = len(arr)
    dp = np.zeros(n)
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1]+arr[i], arr[i])

    print(dp)
    return np.max(dp)

arr = np.array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(int(max_subarray_sum(arr))) # Output: 6
