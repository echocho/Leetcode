# Leetcode349_intersectionOfTwoArrays.py

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution 1: use hashset
        # O(1), worse case O(n)
        set_nums1, set_nums2 = set(nums1), set(nums2)
        return [x for x in set_nums2 if x in set_nums1]

        # Solution 2: use hashset and operator &
        # O(1)
        """
        return list(set(nums1) & set(nums2)) 
        """

s = Solution()
print(s.intersection([1,2,2,1], [2,2]) == [2])
print(s.intersection([2,3,4,2,3], [2,3,4]) == [2,3,4])
print(s.intersection([], [1,2,3]) == [])
print(s.intersection([], []) == [])
print(s.intersection([1,2,3], []) == [])
