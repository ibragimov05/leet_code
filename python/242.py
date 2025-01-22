class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t): return False

		for i, j in t, s:
			if s.count(i) != t.count(j): return False

		return True


print(Solution().isAnagram(s="anagram", t="nagaram"))

# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
