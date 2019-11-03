# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

Class SolutionRecursion:
    def inorder_traversal(self, root):
        res = []
        self.helper(root, res)
        return res 
    
    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
