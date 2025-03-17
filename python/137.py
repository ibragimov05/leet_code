from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_nums = Counter(nums)

        for val, count in count_nums.items():
            if count == 1:
                return val
        return -1
