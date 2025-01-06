class Solution:
	def sortVowels(self, s: str) -> str:
		vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
		vowels_ls = []

		for i in s:
			if i in vowels:
				vowels_ls.append(i)
		print(vowels_ls)
		return ''


print(Solution().sortVowels("lEetcOde"))  # lEOtcede
print(Solution().sortVowels("lYmpH"))  # lYmpH
