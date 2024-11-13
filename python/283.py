class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
