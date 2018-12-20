"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
            stack += [child for child in root.children]
        return res[::-1]
        

