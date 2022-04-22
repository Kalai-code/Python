from typing import List
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
"""
# brute force solution
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    outerlist = []
    totalSum = 0
    if len(nums) > 4:
        nums.sort()
        for a in range(len(nums) - 3):
            for b in range(a+1,len(nums) -2):
                for c in range(b+1,len(nums) -1):
                    for d in range(c+1,len(nums)):
                        totalSum = nums[a] + nums[b] + nums[c] + nums[d]
                        if totalSum ==  target:
                            innerlist = [nums[a],nums[b],nums[c],nums[d]]
                            if innerlist not in outerlist:
                                outerlist.append(innerlist)
        return outerlist
    elif len(nums) == 4:
        if sum(nums) == target:
            outerlist.append(nums)
            return outerlist
        else:
            return []
    else:
        return []
"""
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    outerlist = []
    totalSum = 0
    if len(nums) > 4:
        nums.sort()
        for a in range(len(nums) - 3):
            for b in range(a+1,len(nums) - 2):
                if a > 0 and nums[a] == nums[a - 1]:
                    continue
                (c,d) = (b+1,len(nums) -1)
                while c < d:
                    totalSum = nums[a] + nums[b] + nums[c] + nums[d]
                    if totalSum ==  target:
                        innerlist = [nums[a],nums[b],nums[c],nums[d]]
                        if innerlist not in outerlist:
                            outerlist.append(innerlist)
                    if totalSum > target:
                        d = d -1
                    else:
                        c = c + 1
        return outerlist           
    elif len(nums) == 4:
        if sum(nums) == target:
            outerlist.append(nums)
            return outerlist
        else:
            return []
    else:
        return []
         

print(fourSum([1,0,-1,0,-2,2],0))

print(fourSum([2,2,2,2,2],8))