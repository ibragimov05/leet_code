class Solution:
    def countElements(self, nums: list[int]) -> int:
        nums.sort()
        return max(0, len(nums) - nums.count(nums[0]) - nums.count(nums[-1]))
