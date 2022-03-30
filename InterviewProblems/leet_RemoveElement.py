from typing import List
def removeElement(nums: List[int], val: int) -> int:
    """ Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed."""
    count = 0
    i = 0
    if len(nums) > 0 and val in nums:
        while i < len(nums):
            if nums[i] == val:
                count = count + 1
                nums.pop(i)
                print(nums)
                nums.insert(-1,'_')
                print(nums)
                #nums[i] = "_"
                if i != 0:
                    i=i-1
                else:
                    i = 0
            else:
                i = i+1
        print(nums)
        return len(nums) - count
    else:
        return len(nums)
"""      
# Test case 1 - Output: 2
print(removeElement(nums = [3,2,2,3], val = 3))

# Test case 2 - Output: 5
print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))

# Test case 3 - Output: 2
print(removeElement(nums = [0,1], val = 2))
"""
# Test case 4 - Output: 1
print(removeElement(nums = [4,5], val = 4))
