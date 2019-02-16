class Solution1(object):
    # O(n)
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        counter1, counter2 = collections.Counter(nums1), collections.Counter(nums2)
        for k1 in counter1.keys():
            if k1 in counter2:
                cnt2 = counter2[k1]; cnt1 = counter1[k1]
                if cnt2 - cnt1 <= 0:
                    ans += [k1] * cnt2
                else:
                    ans += [k1] * cnt1
        return ans
           

class Solution2(object):
    """ Follow up 1:
    if the two arrays are already sorted, we can use two pointers to compare items in nums1 and nums2
    O(n)
    """
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return ans
print(Solution2().intersect([1,2,3,6,8,9], [8,10,13])==[8])
print(Solution2().intersect([1,1,2,2], [2,2])==[2,2])
print(Solution2().intersect([1,2], [])==[])
print(Solution2().intersect([], [1,1])==[])
print(Solution2().intersect([3,3,6,9], [1,2,8])==[])

Solution3