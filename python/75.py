class Solution:
	def sortColors(self, nums: list[int]) -> None:
		nums = sorted(nums)

print(Solution().sortColors([2,0,2,1,1,0]))
print(Solution().sortColors([2,0,1]))
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]