import operator
class Solution:
    # use a dictionary, key, value = character, index, if a character appears more than once, set value to -1
    # O(n)
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chrs = dict()
        for index, letter in enumerate(s):
            if letter in chrs.keys():
                chrs[letter] = -1
            else:
                chrs[letter] = index
        for k, v in sorted(chrs.items(), key=operator.itemgetter(1)):
            if v > -1:
                return v
        return -1
        
