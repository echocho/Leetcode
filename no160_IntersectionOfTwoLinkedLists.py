# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # traverse A/B and point to headB/headA; if two pointers will meet if two linked list have intersection
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pointer_a, pointer_b = headA, headB
        while pointer_a != pointer_b:
            pointer_a = headB if not pointer_a else pointer_a.next
            pointer_b = headA if not pointer_b else pointer_b.next
        return pointer_a