class Solution:
	def removeOccurrences(self, s: str, part: str) -> str:
		while True:
			if part in s:
				s = s.replace(part, "", 1)
				print(s)
			else:
				return s
