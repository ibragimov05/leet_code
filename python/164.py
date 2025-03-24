from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        if len(nums) < 2:
            return 0

        return max(nums[i + 1] - nums[i] for i in range(len(nums) - 1))
