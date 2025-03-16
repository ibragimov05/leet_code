class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words: list[str] = s.split(" ")

        for i in range(len(reversed_words)):
            reversed_words[i] = reversed_words[i][::-1]

        return " ".join(reversed_words)
