class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) == 1:
                return i
        return nums[0]
