from typing import List
"""
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    outlist = []
    found = 0
    for i in range(len(nums1)):
        jindex = nums2.index(nums1[i])
        if jindex < len(nums2) - 1:
            if nums2[jindex + 1] > nums1[i]:
                outlist.append(nums2[jindex+1])
            else:
                while jindex < len(nums2) - 1:
                    if nums2[jindex + 1] > nums1[i]:
                        outlist.append(nums2[jindex + 1])
                        found = 1
                        break
                    jindex = jindex + 1
                if found == 0:
                    outlist.append(-1)
        else:
            outlist.append(-1)
    return outlist
"""
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    outlist = []   
    for i in nums1:
        nums2_index = nums2.index(i)
        if nums2_index < len(nums2) - 1:
            found = 0
            for j in nums2[nums2_index:]:
                if j > i:
                    outlist.append(j)
                    found = 1
                    break
            if found == 0:
                outlist.append(-1)
        else:
            outlist.append(-1)
    return outlist
        
print(nextGreaterElement([4,1,2],[1,3,4,2]))

print(nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))

print(nextGreaterElement([2,1,3],[2,3,1]))