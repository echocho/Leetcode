# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head, head.next = ListNode(0), head
        c = head
        while c.next:
            if c.next.val == val:
                c.next = c.next.next
            else: c = c.next
        return head.next


# 203Remove_Linked_List_Elements.py



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    # need to traverse the whole list, as may need to remove multiple items from the linked list
    # o()
    current = head
    previous = None
    while head:
        if current.val != val:
            previous = current
            current = current.next
        else:
            if previous == None:
                head = head.next
            else:
                previous.next = current.next

    return head





















