class Solution:
	def stringMatching(self, words: list[str]) -> list[str]:
		result = []

		for word in words:
			if word in words:
				result.append(word)

		return result

print(Solution().stringMatching(["mass","as","hero","superhero"]))
print(Solution().stringMatching(["leetcode","et","code"]))
print(Solution().stringMatching( ["blue","green","bu"]))

# Example 1:
#
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:
#
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:
#
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
