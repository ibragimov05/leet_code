class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted_words = s.split(" ")

        for i in range(len(splitted_words) - 1, -1, -1):
            if splitted_words[i] == "":
                continue
            else:
                return len(splitted_words[i])
        return 0


s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
