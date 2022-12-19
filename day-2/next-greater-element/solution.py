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



if __name__ == '__main__':
    nums1 = [[4,1,2], [2,4], [8, 5, 77, 69]]
    nums2 = [[1,3,4,2],[1,2,3,4], [5, 8, 75, 14, 69, 10, 33, 77]]
    sol = Solution()

    for i in range(len(nums1)):
        print(sol.nextGreaterElement(nums1[i], nums2[i]))