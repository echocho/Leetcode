# Leetcode863_AllNodesDistanceKinBinaryTree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def distanceK(root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    # Solution 1: BFS
    if not root:
        return []

    n, q = 1, []
    q.append(root)

    if root.val == target:
        q.pop(0)
        q.append(root.left)


    if root.val == target:
        n = 0

    q.append(root)
    while q:
        q.pop(0)
        q.append(root.left)
        q.append(root.right)



