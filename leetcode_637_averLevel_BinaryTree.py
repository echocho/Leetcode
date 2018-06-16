# leetcode_637_averLevel_BinaryTree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        else:
            aver = [(m+n)/2 for m, n in self.averageOfLevels(root.right), self.averageOfLevels(root.left)]
            

        return res[::-1]
        