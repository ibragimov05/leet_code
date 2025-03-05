class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for char in letters:
            if ord(char) > ord(target):
                return char
        return letters[0]
