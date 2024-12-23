class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        return [word for word in words if any(set(word.lower()) <= i for i in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')])]
