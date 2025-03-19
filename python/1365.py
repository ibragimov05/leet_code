from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums: List[int] = sorted(nums)

        count: dict = {}

        for idx, num in enumerate(sorted_nums):
            if num not in count:
                print(count)
                count[num] = idx

        return [count[num] for num in nums]
