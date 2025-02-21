from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicated_numbers = set()

        for number in nums:
            if number in seen and number not in duplicated_numbers:
                duplicated_numbers.add(number)
            seen.add(number)

        return list(duplicated_numbers)
