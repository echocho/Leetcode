# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # get all leaf vals of both tree and then compare
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaves(root):
            if not root:
                return False
            vals, stack = [], [root,]
            while len(stack):
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if not node.left and not node.right:
                    vals.append(node.val)
            return vals
        return get_leaves(root1) == get_leaves(root2)
                
                