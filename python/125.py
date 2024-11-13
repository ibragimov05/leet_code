class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ""

        for i in s.lower():
            if (ord(i) >= 48 and 57 >= ord(i)) or (97 <= ord(i) and 122 >= ord(i)):
                alphanumeric += i

        return alphanumeric == alphanumeric[::-1]
