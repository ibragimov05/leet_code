from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        transformed_array: List[int] = []

        for number in nums:
            if number % 2 == 0:
                transformed_array.append(0)
                continue
            transformed_array.append(1)

        return sorted(transformed_array)
