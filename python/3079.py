from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sum_of_encrypted: int = 0

        for num in nums:
            digits: List[int] = [int(d) for d in str(num)]
            max_digit: int = max(digits)
            encrypted = int(str(max_digit) * len(digits))
            sum_of_encrypted += encrypted

        return sum_of_encrypted
