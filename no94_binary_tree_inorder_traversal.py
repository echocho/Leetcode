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

Class SolutionCallStack:
    def inorder_traversal(self, root):
        call_stack = []
        vals = []
        next_exec = 'CHECK_NULL'
        while next_exec or len(call_stack):
            if next_exec == 'CHECK_NULL':
                if not root:
                    if not call_stack:
                        break
                    root, next_exec = call_stack.pop()
                else:
                    next_exec = 'LEFT'
            elif next_exec == 'LEFT':
                call_stack.append((root, 'APPEND_VAL'))
                root = root.left
                next_exec = 'CHECK_NULL'
            elif next_exec == 'APPEND_VAL':
                vals.append(root.val)
                next_exec = 'RIGHT'
            elif next_exec == 'RIGHT':
                call_stack.append((root, None))
                root = root.right
                next_exec = 'CHECK_NULL'
            else:
                root, next_exec = call_stack.pop()             
        return vals
