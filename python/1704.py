class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        first_half, second_half = 0, 0
        s_len = len(s)

        for i in range(s_len // 2):
            if s[i] in vowels:
                first_half += 1
            if s[s_len // 2 + i] in vowels:
                second_half += 1

        return first_half == second_half
