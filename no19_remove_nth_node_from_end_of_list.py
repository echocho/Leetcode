# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iterate once, get linked list length
	# iterate again, remove node(s) from list
    # O(L) where L is length of n
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = self.getListLength(head) 
        length -= n
        first = dummy

        while length > 0:
            first = first.next
            length -= 1
        first.next = first.next.next
        
        return dummy.next
    
    def getListLength(self, head):
        list_len = 0
        first = head
        while first:
            list_len += 1
            first = first.next
        return list_len