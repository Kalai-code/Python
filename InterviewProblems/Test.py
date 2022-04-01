from typing import List
"""You are given an integer array nums.
The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

"""
#solution 1
def sumOfUnique(nums: List[int]) -> int:
    dictNum = {}
    count = 0
    for num in nums:
        if num in dictNum:
            dictNum[num] +=1
        else:
            dictNum[num] = 1
    for dnum in dictNum:
        if dictNum[dnum] == 1:
            count = count + dnum
    return count
#solution 2
def sumOfUnique2(nums: List[int]) -> int:
    count = 0
    for num in nums:
        if nums.count(num) == 1:
            count = count + num
    return count
    
print(sumOfUnique([1,2,3,2]))

print(sumOfUnique2([1,2,3,2]))

"""
"""