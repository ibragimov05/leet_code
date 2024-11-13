class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
