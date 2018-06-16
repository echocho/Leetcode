# Leetcode141_linkedListCycle.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # Solution 1:
    # iterate and put head in a hashset
    # if there is a cycle, we will have a duplicate element
    # meaning the node we are pointing to is the same as the one in the set

    # O(n)

    if head == None: return False
    nodesChecked = set()
    while head:
        if head in nodesChecked:
            return True
        nodesChecked.add(head)
        head = head.next
    return False



