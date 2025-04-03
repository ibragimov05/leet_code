from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum_of_good_numbers: int = 0
        n: int = len(nums)

        for i in range(n):
            if (i - k >= 0 and nums[i] <= nums[i - k]) or (
                i + k < n and nums[i] <= nums[i + k]
            ):
                continue

            sum_of_good_numbers += nums[i]

        return sum_of_good_numbers
