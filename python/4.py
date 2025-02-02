class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		nums1.extend(nums2)
		nums1.sort()

		len_nums = len(nums1)

		if len_nums % 2 != 0:
			return nums1[len_nums // 2]
		else:
			mid1 = nums1[len_nums // 2 - 1]
			mid2 = nums1[len_nums // 2]
			return (mid1 + mid2) / 2
