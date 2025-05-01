class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = {}
        i = 0
        for c in key:
            if c != " " and c not in alphabet:
                alphabet[c] = chr(i + ord("a"))
                i += 1

        result: list[str] = []

        for c in message:
            if c == ' ':
                result.append(' ')
            else:
                result.append(alphabet[c])

        return "".join(result)


print(Solution().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))

# Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".
