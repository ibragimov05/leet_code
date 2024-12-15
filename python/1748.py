class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(num for num in nums if nums.count(num) == 1)
