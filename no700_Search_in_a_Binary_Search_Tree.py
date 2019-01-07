# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        stack = [root,]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return []
                
