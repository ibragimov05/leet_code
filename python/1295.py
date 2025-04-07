from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_of_even_digits: int = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count_of_even_digits += 1

        return count_of_even_digits
