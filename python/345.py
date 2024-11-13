class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1

            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        return "".join(chars)


s = Solution()
print(s.reverseVowels("IceCreAm"))

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
