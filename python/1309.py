class Solution:
    def freqAlphabets(self, s: str) -> str:
        res: list[str] = []
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                val = int(s[i : i + 2])
                res.append(chr(val + 96))
                i += 3
            else:
                res.append(chr(int(s[i]) + 96))
                i += 1

        return "".join(res)
