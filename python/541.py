class Solution:
	def reverseStr(self, s: str, k: int) -> str:
		return s[::k]


print(Solution().reverseStr("abcdefg", 2))
# Example 1:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
#
# Input: s = "abcd", k = 2
# Output: "bacd"
