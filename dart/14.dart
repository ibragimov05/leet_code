class Solution {
  const Solution._();

  String longestCommonPrefix(List<String> strs) {
    if (strs.isEmpty) return "";
    var prefix = strs[0];

    for (var i = 1; i < strs.length; i++) {
      while (!strs[i].startsWith(prefix)) {
        prefix = prefix.substring(0, prefix.length - 1);
        if (prefix.isEmpty) return "";
      }
    }

    return prefix;
  }
}
