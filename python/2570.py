from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged_dict: dict[int, int] = {}

        for id_value, value in nums1:
            merged_dict[id_value] = merged_dict.get(id_value, 0) + value

        for id_value, value in nums2:
            merged_dict[id_value] = merged_dict.get(id_value, 0) + value

        return sorted([[key, value] for key, value in merged_dict.items()])
