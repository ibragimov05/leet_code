from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0

        return [num for num in nums if num != 0] + [0] * nums.count(0)
