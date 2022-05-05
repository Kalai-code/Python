#Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K
"""
Example 1:

Input:
N = 5, K = 3
arr[] = [1,2,3,4,5]
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
"""
def reverseInGroups(arr, N, K):
    # code here
    index = 0
    for i in range(0,N,K):
        arr1 = arr[i:i+K][::-1]
        arr[i:i+K] = arr1[:]
        print(arr)  
    return arr

print(reverseInGroups([1,2,3,4,5],5,3))