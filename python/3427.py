from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sub_sum: int = 0

        for i in range(len(nums)):
            start: int = max(0, i - nums[i])

            sub_sum += sum(nums[start : i + 1])

        return sub_sum
