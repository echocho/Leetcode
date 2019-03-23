# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use fast and slow pointers to find the mid
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        node = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = node
            node = curr
            
        # compare the two halves
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True