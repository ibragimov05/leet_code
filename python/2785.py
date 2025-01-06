class Solution:
	def sortVowels(self, s: str) -> str:
		vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
		sorted_vowels = iter(sorted([char for char in s if char in vowels]))

		return ''.join(next(sorted_vowels) if char in vowels else char for char in s)
