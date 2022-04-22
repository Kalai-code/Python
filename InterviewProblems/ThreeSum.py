from typing import List

"""
# brute force solution --> gives Time Limit Exceeded error for lengthier list
def threeSum(nums: List[int]) -> List[List[int]]:
    innerlist = []
    outerlist = []
    if len(nums) > 3:
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i+1,len(nums) - 1):
                for k in range(j+1,len(nums)):
                    innerlist = []
                    if nums[i] + nums[j] + nums[k] == 0:
                        innerlist.append(nums[i])
                        innerlist.append(nums[j])
                        innerlist.append(nums[k])
                        if innerlist not in outerlist:
                            outerlist.append(innerlist)
        return outerlist
    elif len(nums) == 3:
        if sum(nums) == 0:
            innerlist = nums.copy()
            outerlist.append(innerlist)
            return outerlist
        else:
            return [] 
    else:
        return []
"""
"""
# another approach
def threeSum(nums: List[int]) -> List[List[int]]:
    outerlist = []
    threesum = 0
    if len(nums) > 3:
        nums.sort()
        for i in range(len(nums) - 2):            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j,k = i+1,len(nums)-1
            print(j,k)
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0:
                    outerlist.append([nums[i],nums[j],nums[k]])
                    k = k - 1
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1
                elif threesum > 0:
                    k = k - 1
                else:
                    j = j + 1
        return outerlist
    elif len(nums) == 3:
        if sum(nums) == 0:
            outerlist.append(nums)
            return outerlist
        else:
            return [] 
    else:
        return []
"""
def threeSum(nums: List[int]) -> List[List[int]]:
        outerlist = []
        threesum = 0
        for i in range(len(nums) - 2):  
            nums.sort()
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j,k = i+1,len(nums)-1
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0:
                    outerlist.append([nums[i],nums[j],nums[k]])
                    k = k - 1
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1
                elif threesum > 0:
                    k = k - 1
                else:
                    j = j + 1
        return outerlist

print(threeSum([0,0,0]))

print(threeSum([-1,0,1,2,-1,-4]))