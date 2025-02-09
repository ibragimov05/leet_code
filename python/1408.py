class Solution:
	def stringMatching(self, words: list[str]) -> list[str]:
		return list(
			set(
				words[i]
				for i in range(len(words))
				for j in range(len(words))
				if words[i] != words[j] and words[i] in words[j]
			)
		)
