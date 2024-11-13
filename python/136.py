class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) == 1:
                return i
        return nums[0]


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
