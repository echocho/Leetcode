# Leetcode567_permutationInString.py

import collections

def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    s1_counter = collections.Counter(s1)
    s2_counter = collections.Counter(s2[:len(s1)-1])

    for i in range(len(s1)-1, len(s2)):
        s2_counter[s2[i]] += 1

        if s2_counter == s1_counter:
            return True
        s2_counter[s2[i-len(s1)+1]] -= 1

        if s2_counter[s2[i-len(s1)+1]] == 0:
            del s2_counter[s2[i-len(s1)+1]]
    return False

print(checkInclusion('ab', 'eidbaooo'))
print(checkInclusion('ab', 'eidboaoo'))