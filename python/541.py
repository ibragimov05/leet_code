class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reversed_str: list[str] = []
        should_add: bool = True

        for i in range(0, len(s), k):
            if should_add:
                reversed_str.append(s[i : i + k][::-1])
                should_add = False
            else:
                reversed_str.append(s[i : i + k])
                should_add = True

        return "".join(reversed_str)
