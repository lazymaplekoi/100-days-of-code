from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0, 1]

        for i in range(len(nums)):
            num = nums[i]
            j = i+1
            diff = abs(target - num)

            subset = nums[i+1:]

            if diff in subset:
                j = subset.index(diff)
            elif -diff in subset:
                j = subset.index(-diff)

            if (j+i+1) < len(nums) and nums[i] + nums[j+i+1] == target: return [i, j+i+1]

        return [i, j]
                
test_cases = [([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6), ([-1,-2,-3,-4,-5], -8), ([-3,4,3,90], 0), ([-11,7,3,2,1,7,-10,11,21,3], 11)]

if __name__ == '__main__':
    sol = Solution()
    for nums, target in test_cases:
        print(sol.twoSum(nums, target))