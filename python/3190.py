from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation_count: int = 0

        for number in nums:
            remainder: int = number % 3
            if remainder != 0:
                operation_count += 1

        return operation_count
