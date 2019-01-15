# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def depth(root):
            if not root:
                return 0
            right = depth(root.right)
            left = depth(root.left)
            self.ans = max(right + left, self.ans)
            return max(left, right) + 1 
        
        depth(root)
        return self.ans