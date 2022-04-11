# Leetcode problem 26 - Remove Duplicates from Sorted Array
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    distinctNum = len(set(nums))
    for i in nums:
        countNum = nums.count(i)
        if countNum > 1:
            while countNum > 1:
                index = nums.index(i)
                nums.pop(index)
                countNum = countNum - 1
    print(nums)
    return distinctNum


print(removeDuplicates([1,1,2]))    