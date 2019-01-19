# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return False
        if not s:
            return False
        if self.isIdentical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isIdentical(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return r1.val == r2.val and self.isIdentical(r1.left, r2.left) and self.isIdentical(r1.right, r2.right)
    
    