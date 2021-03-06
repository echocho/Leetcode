# leetcode_104_maxDepthOfBinaryTree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
           return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

            
# 2019-01-13 did it one more time
def maxDepth(root):
    if not root:
        return 0
    
    left, right = maxDepth(root.left), maxDepth(root.right)
    if left > right:
        return 1 + left
    return 1 + right


