class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        reversed_x = int(str(x)[::-1])

        if not self.is_within_32_bit_range(reversed_x) or not self.is_within_32_bit_range(x):
            return 0

        return -reversed_x if is_negative else reversed_x

    @staticmethod
    def is_within_32_bit_range(x) -> bool:
        return -(2**31) <= x <= 2**31 - 1
