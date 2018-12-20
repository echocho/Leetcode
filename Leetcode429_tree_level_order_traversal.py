"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        output, current_vals, current = [], [], [root]
        while current:
            next_level = []
            for root in current:
                if root.children:
                    next_level += root.children
                current_vals.append(root.val)
            output.append(current_vals)
            current, next_level, current_vals = next_level, [], []
        return output 