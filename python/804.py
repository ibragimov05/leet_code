class Solution:
	def uniqueMorseRepresentations(self, words: list[str]) -> int:
		letter_to_morse_alphabet = {
			"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
			"f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
			"k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
			"p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
			"u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
			"z": "--.."
		}

		letter_to_morse = []
		for word in words:
			res_word = ""
			for letter in word:
				res_word += letter_to_morse_alphabet[letter]
			letter_to_morse.append(res_word)

		print(letter_to_morse)
		return 1


print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(Solution().uniqueMorseRepresentations(["a"]))

# Example 1:
#
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
# Example 2:
#
# Input: words = ["a"]
# Output: 1
