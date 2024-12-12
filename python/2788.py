class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        return [word for word in separator.join(words).split(separator) if word != '']
