class Solution:
    def romanToInt(self, s: str) -> int:
        int_roman_dict: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result_sum: int = 0
        prev_val: int = 0

        for roman in s[::-1]:
            current_value: int = int_roman_dict[roman]
            if prev_val > current_value:
                result_sum -= current_value
            else:
                result_sum += current_value
            prev_val = current_value

        return result_sum
