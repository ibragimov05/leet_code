class Solution {
  List<int> topKFrequent(List<int> nums, int k) {
    final count = <int, int>{};

    for (final each in nums) {
      count[each] = (count[each] ?? 0) + 1;
    }

    final res = count.entries.toList()..sort((a, b) => b.value.compareTo(a.value));
    print(res);

    return res.take(k).map((e) => e.key).toList();
  }
}
