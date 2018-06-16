# Leetcode141_linkedListCycle.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None: return False
    nodesChecked = set()
    while head:
        if head in aSet:
            return True
        nodesChecked.add(head)
        head = head.next
    return False

    # Solution 2
    if head == None: return False
    fastPointer = head.next
    slowPointer = head
    while slowPointer != fastPointer:
        if slowPointer == None or fastPointer == None:
            return False
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return True



