""" Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""
from typing import List
def maxSubArray_try1(nums: List[int]) -> int:
    MaxNum = max(nums)
    for i in range(len(nums)):
        j = i+1
        SumSubArray = nums[i]
        while j < len(nums):
            SumSubArray = SumSubArray + nums[j]
            if SumSubArray > MaxNum:
                MaxNum = SumSubArray
            j = j+1
    return MaxNum

def maxSubArray(nums: List[int]) -> int:  
    curr = 0
    maxSum =  sum(nums)
    for i in nums:
        curr = max(i, curr + i)
        maxSum = max(curr,maxSum)
    return maxSum
        
print(maxSubArray([5,4,-1,7,8]))