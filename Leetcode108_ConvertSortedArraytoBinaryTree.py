# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # the middle of arrary will be the root, left half of nums will be the left sub tree 
    # and the right, the right,
    # do this recursively
    # Time Complexity: O(nlogn)
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        indx_mid = len(nums) // 2
        root = TreeNode(nums[indx_mid])
        root.left = self.sortedArrayToBST(nums[: indx_mid])
        root.right = self.sortedArrayToBST(nums[indx_mid + 1 :])

        return root

