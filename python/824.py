class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        words = sentence.split()

        got_latin_words = [
            (word + "ma" if word[0] in vowels else word[1:] + word[0] + "ma")
            + "a" * (i + 1)
            for i, word in enumerate(words)
        ]

        return " ".join(got_latin_words)
