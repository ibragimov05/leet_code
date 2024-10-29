class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        max_number = max(nums)

        for i in range(max_number):
            if i not in nums:
                return i
            else:
                nums.remove(i)

        return max_number + 1


s = Solution()
print(s.missingNumber([3, 0, 1]))
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.
