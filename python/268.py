class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        max_number = max(nums)

        for i in range(max_number):
            if i not in nums:
                return i
            else:
                nums.remove(i)

        return max_number + 1
