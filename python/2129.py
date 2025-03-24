class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result: list[str] = []
        for word in title.split(" "):
            if len(word) <= 2:
                result.append(word.lower())
            else:
                result.append(word.capitalize())
        return " ".join(result)
