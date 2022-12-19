from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for i in range(len(nums1))]
        
        for i in range(len(nums1)):
            num = nums1[i]
            index = nums2.index(num)

            # no next greater element if it's the max or the last element
            if num == max(nums2) or index == len(nums2)-1: continue

            for j in range(index+1, len(nums2)):
                if nums2[j] > num:
                    ans[i] = nums2[j]
                    break
        return ans