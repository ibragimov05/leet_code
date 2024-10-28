class Solution(object):
    def scoreOfString(self, s):
        sum: int = 0
        for i in range(len(s) - 1):
            left_ord = ord(s[i])
            right_ord = ord(s[i + 1])
           
            if left_ord < right_ord:
                sum += right_ord - left_ord
            else:
                sum += left_ord - right_ord
        
        return sum


s = Solution()
print(s.scoreOfString("hello"))
# Input: s = "hello"
# Output: 13
# Explanation:
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111.
# So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| =
# 3 + 7 + 0 + 3 = 13.
