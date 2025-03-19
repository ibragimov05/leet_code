from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_nums_count: List[int] = []

        for i in range(len(nums)):
            count: int = 0

            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    continue
                if nums[i] > nums[j]:
                    count += 1

            smaller_nums_count.append(count)

        return smaller_nums_count
