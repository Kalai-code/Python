from typing import List

def findGCD(nums: List[int]) -> int:
    minNum = min(nums)
    maxNum = max(nums)
    i = GCF = 1
    minGCF = minNum
    maxGCF = maxNum
    while maxNum >= i:
        if maxGCF % minGCF == 0:
            GCF = minGCF * i
            return GCF
        elif (minGCF % i == 0) and (maxGCF % i == 0):
            minGCF = minGCF/i
            maxGCF = maxGCF/i
            GCF = GCF * i
        i = i + 1
    return int(GCF)
    
print(findGCD([8,5,8,7,4]))

print(findGCD([2,5,6,9,10]))

print(findGCD([7,5,6,8,3]))

print(findGCD([3,3]))