# Leetcode496_nextGreaterElement1.py
def nextGreaterElement(nums1, nums2):
    # # did it myself, a slow verion
    # ans = []
    # for digit in nums1:
    #     # print('digit: ', digit)
    #     in_nums2 = nums2.index(digit)
    #     # print('in_nums2: ', in_nums2)
    #     frag = nums2[in_nums2+1:]
    #     # print('frag: ', frag)
    #     if in_nums2 == len(nums2)-1:
    #         ans.append(-1)
    #     # print('ans: ', ans)
    #     for num in frag:
    #         # print('num: ', num)
    #         if num > digit:
    #             ans.append(num)
    #             # print('ans: ', ans)
    #             break
    #     if len(ans) != len(nums1[: nums1.index(digit)+1]):
    #         ans.append(-1)
    #         # print('not equal length: ', len(ans) != len(nums1[: nums1.index(digit)+1]))
    #         # print('final ans: ', ans)

    # return ans
    
    # a faster version
    mapping = {}
    for i in range(len(nums2)):
        for j in range(i, len(nums2)):
            if nums2[j] > nums2[i]:
                mapping[nums2[i]] = nums2[j]
                break
            if j == len(nums2) - 1:
                mapping[nums2[i]] = -1
    res = []
    for i in range(len(nums1)):
        res.append(mapping[nums1[i]])
    return res




print(nextGreaterElement([4,1,2], [1,3,4,2]))
print(nextGreaterElement([2,4], [1,2,3,4]))
print(nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapping = {}
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    mapping[nums2[i]] = nums2[j]
                    break
                if j == len(nums2) - 1:
                    mapping[nums2[i]] = -1
        res = []
        for i in range(len(nums1)):
            res.append(mapping[nums1[i]])
        return res