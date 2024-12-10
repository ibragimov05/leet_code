class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        negative_numbers, positive_numbers = 0, 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_numbers += 1
            else:
                break

        return max(negative_numbers, len(nums) - negative_numbers - nums.count(0))
