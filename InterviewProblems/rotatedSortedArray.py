"""
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""
from typing import List
"""
#solution 1
def search(nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        else:
            return False
"""         
# solution 2 - linear search
def search(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) -1
    while left < right:
        if nums[left] == target:
            return True
        elif nums[right] == target:
            return True
        else:
            left = left + 1
            right = right - 1
    return False

print(search([2,5,6,0,0,1,2],3))