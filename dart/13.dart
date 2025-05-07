class Solution {
  int romanToInt(String s) {
    Map<String, int> romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000};
    int totalSum = 0;
    int prevVal = 0;

    for (var i = s.length - 1; i >= 0; i--) {
      int curVal = romanDict[s[i]] ?? 0;

      if (curVal < prevVal) {
        totalSum -= curVal;
      } else {
        totalSum += curVal;
      }
      prevVal = curVal;
    }

    return totalSum;
  }
}
