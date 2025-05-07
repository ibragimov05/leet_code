class Solution {
  int lengthOfLongestSubstring(String s) {
    int maxLen = 0;
    int start = 0;
    Set<String> seen = <String>{};

    for (int end = 0; end < s.length; end++) {
      while (seen.contains(s[end])) {
        seen.remove(s[start]);
        start++;
      }

      seen.add(s[end]);
      maxLen = maxLen > (end - start + 1) ? maxLen : (end - start + 1);
    }

    return maxLen;
  }
}
