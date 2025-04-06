class Solution:
    def countDigits(self, num: int) -> int:
        count: int = 0
        for digit in str(num):
            if num % int(digit) == 0:
                count += 1
        return count


print(Solution().countDigits(7))
print(Solution().countDigits(121))
print(Solution().countDigits(1248))

# Example 1:

# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

# Example 2:

# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

# Example 3:

# Input: num = 1248
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
