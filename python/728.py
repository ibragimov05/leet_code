from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers: List[int] = []

        for i in range(left, right + 1):
            is_self_dividing_digit = True

            for char in str(i):
                int_char: int = int(char)
                if not (int_char != 0 and i % int_char == 0):
                    is_self_dividing_digit = False
                    break
            if is_self_dividing_digit:
                numbers.append(i)

        return numbers
