from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array: List[int] = []

        for i in range(0, n):
            shuffled_array.extend([nums[i], nums[i + n]])

        return shuffled_array
