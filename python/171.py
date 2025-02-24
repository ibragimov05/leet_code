class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result: int = 0

        for letter in columnTitle:
            result = result * 26 + (ord(letter) - ord("A") + 1)

        return result


# print(Solution().titleToNumber("A"))
# print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("ZY"))
# print(Solution().titleToNumber("AA"))
# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701
