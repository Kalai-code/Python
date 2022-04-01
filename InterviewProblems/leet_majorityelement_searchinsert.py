from typing import List
"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

def majorityElement(nums: List[int]) -> int:
    numDict = {}
    for num in nums:
        if num in numDict:
            numDict[num] +=1
        else:
            numDict[num] = 1
    return max(numDict, key=numDict.get)

# Test case 1 Output: 3
print(majorityElement([3,3,4]))

# Test case 1 Output: 3
print(majorityElement([3,2,3]))

# Test case 1 Output: 2
print(majorityElement([2,2,1,1,1,2,2]))


"""Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order."""

def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    elif target > max(nums):
        return len(nums)
    elif target < min(nums):
        return 0
    else:   
        for i in range(len(nums)):
            if nums[i] < target and nums[i+1] > target:
                return i+1
                
#Test case 1 - Output: 2
print(searchInsert([1,3,5,6],5))

#Test case 1 - Output: 1
print(searchInsert([1,3,5,6],2))

#Test case 1 - Output: 4
print(searchInsert([1,3,5,6],7))

#Test case 1 - Output: 0
print(searchInsert([1,3,5,6],0))