class Solution {
  List<List<String>> groupAnagrams(List<String> strs) {
    final map = <String, List<String>>{};

    for (final str in strs) {
      final sorted = str.split('')..sort();
      map.putIfAbsent(sorted.join(), () => []);
      map[sorted.join()]!.add(str);
    }

    return map.values.toList();
  }
}
