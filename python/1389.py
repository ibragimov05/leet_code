from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_array: list[int] = []

        for num, index in zip(nums, index):
            target_array.insert(index, num)

        return target_array
