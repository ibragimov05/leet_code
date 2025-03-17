from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for _, count in Counter(nums).items():
            if count % 2 != 0:
                return False
        return True
