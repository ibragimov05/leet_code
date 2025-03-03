from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_nums: list[int] = []
        bigger_nums: list[int] = []
        p_count: int = 0

        for number in nums:
            if number > pivot:
                bigger_nums.append(number)
            elif number < pivot:
                smaller_nums.append(number)
            else:
                p_count += 1

        return smaller_nums + ([pivot] * p_count) + bigger_nums
