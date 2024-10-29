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
