# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
	# iterative
    # get vals using inorder traversal and create a new tree
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
	    # get all node vals 
        vals, stack, node = [], [], root
        while stack or node:
            if node:
            	stack.append(node)
            	node = node.left
            else:
            	node = stack.pop()
            	vals.append(node.val)
            	node = node.right
        # build a new trew
        vals.sort()
        cur = res = TreeNode(None)
        for i in vals:
            cur.right = TreeNode(i)
            cur = cur.right
        return res.right