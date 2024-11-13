class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum([nums[j] for j in range(i + 1)]) for i in range(len(nums))]
