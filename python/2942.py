class Solution:
	def findWordsContaining(self, words: list[str], x: str) -> list[int]:
		res: list[int] = []
		for i in range(len(words)):
			if x in words[i]:
				res.append(i)
		return res


print(Solution().findWordsContaining(["leet", "code"], "e"))  # [0, 1]
print(Solution().findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))  # [0, 2]
print(Solution().findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z"))  # []
