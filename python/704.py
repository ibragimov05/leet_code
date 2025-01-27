class Solution:
	def search(self, nums: list[int], target: int) -> int:
		return self.__binary_search(nums, 0, len(nums) - 1, target)

	def __binary_search(self, arr: list[int], low: int, high: int, x: int) -> int:
		if high >= low:
			mid = (high + low) // 2

			if arr[mid] == x:
				return mid
			elif arr[mid] > x:
				return self.__binary_search(arr, low, mid - 1, x)
			else:
				return self.__binary_search(arr, mid + 1, high, x)
		else:
			return -1
