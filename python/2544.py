class Solution:
	def alternateDigitSum(self, n: int) -> int:
		list_n = list(map(int, str(n)))
		return sum(list_n[i] if i % 2 == 0 else list_n[i] * -1 for i in range(len(list_n)))
