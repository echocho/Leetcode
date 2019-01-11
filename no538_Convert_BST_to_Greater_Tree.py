# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
        # iterate the tree twice
        # first time: get all vals 
        # second time: modify node.vals
        # NOT EFFICIENT ENOUGH THOUGH
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        vals, stack = [], [root,]
        # first time
        while stack:
            node = stack.pop()
            vals.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.r7ht)
        # second time
        stack = [root,]
        while stack:
            node = stack.pop()
            node.val += sum([i for i in vals if i > node.val])
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

class Solution3:
    # recursive revser in order tree traversal
    def __init__(self):
        self.total = 0
    
    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
=======
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterate the tree only once
        # reverse in-order traversal
        if not root:
            return None
        sum, stack, node = 0, [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                sum += node.val
                node.val = sum
                node = node.left
>>>>>>> a5a0d1753d275d9a4689133acae2114d39aa950a
        return root
