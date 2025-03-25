from math import gcd
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return max(nums) if min(nums) == 0 else gcd(min(nums), max(nums) % min(nums))
