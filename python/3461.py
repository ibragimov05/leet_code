class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            new_s_list: list[str] = []

            for i in range(len(s) - 1):
                new_s_list.append(str((int(s[i]) + int(s[i + 1])) % 10))

            s = "".join(new_s_list)

        return s[0] == s[1]
