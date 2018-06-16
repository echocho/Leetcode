# Leetcode501_findModeInBinarySearchTree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findMode(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root: return []
    stack = [root]
    mode = {}
    while stack:
        node = stack.pop()
        mode[node.val] = mode.get(node.val, 0) + 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    max_cnt = max(mode.values())
    return [m for m, v in mode.items() if v == max_cnt]
