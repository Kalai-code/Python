from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target"""
    sumlist = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                sumlist.append(i)
                sumlist.append(j)
                return sumlist
    return sumlist


print(twoSum([1,2,3],5))

def isPalindrome(x: int) -> bool:
    """Given an integer x, return true if x is palindrome integer."""
    x = str(x)
    if x == x[::-1]:
        return  True
    else:
        return False
        
print(isPalindrome(-121))