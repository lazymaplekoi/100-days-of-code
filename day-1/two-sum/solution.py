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