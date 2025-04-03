from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n: int = len(nums)

        partitions_count: int = 0

        for i in range(n - 1):
            left_subarray: int = sum(nums[0 : i + 1])
            right_subarray: int = sum(nums[i + 1 : n])

            if (left_subarray - right_subarray) % 2 == 0:
                partitions_count += 1

        return partitions_count
