class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet: dict[str, str] = {}
        i = 0
        for c in key:
            if c != " " and c not in alphabet:
                alphabet[c] = chr(i + ord("a"))
                i += 1

        result: list[str] = []

        for c in message:
            if c == " ":
                result.append(" ")
            else:
                result.append(alphabet[c])

        return "".join(result)
