from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1).difference(set(nums2))
        set_nums2 = set(nums2).difference(set(nums1))

        return [list(set_nums1), list(set_nums2)]
