# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if not floor < root.val < ceiling:
            return False

        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)