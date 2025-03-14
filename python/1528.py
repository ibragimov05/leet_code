from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indices_len: int = len(indices)
        restored_str: List[str] = [""] * indices_len

        for i in range(indices_len):
            restored_str[indices[i]] = s[i]

        return "".join(restored_str)
