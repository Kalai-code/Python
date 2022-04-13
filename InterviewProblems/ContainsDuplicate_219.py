# Problem -  219. Contains Duplicate II
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import List
# This logic gave time limit exceeded error
"""
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
	dict = {}
	for i in range(len(nums)):
		if nums.count(nums[i]) > 1:
			if nums[i] not in dict:
				dict[nums[i]] = i
			elif nums[i] in dict:
				if abs(i - dict[nums[i]]) <= k:
					return True
				else:
					dict[nums[i]] = i
	return False
"""
# This worked
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
	dict = {}
	for i in range(len(nums)):
			if nums[i] in dict and abs(i - dict[nums[i]]) <= k:				        
				return True
			else:
				dict[nums[i]] = i
	return False
    
print(containsNearbyDuplicate([1,2,3,1,2,3],2))
				
		