class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(num for num in nums if nums.count(num) == 1)


print(Solution().sumOfUnique([1, 2, 3, 2]))
print(Solution().sumOfUnique([1, 1, 1, 1, 1]))
print(Solution().sumOfUnique([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5]))

# Example 1:
#
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:
#
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:
#
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
