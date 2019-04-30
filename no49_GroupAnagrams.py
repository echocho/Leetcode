# solution: strings are anagrams if and only if their occurrences of characters are the same
# use tuple(occurances(0or1) of each character) as key of hashmap

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        d = defaultdict(list)
        for item in strs:
            occurance = [0] * 26
            for c in item:
                occurance[ord(c) - ord('a')] += 1
            d[tuple(occurance)].append(item)
        return list(d.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(["eat", "tea", "tan"]))