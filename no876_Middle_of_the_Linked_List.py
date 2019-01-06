# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes_dict, cnt = {}, 0
        while head:
            cnt += 1
            nodes_dict[cnt] = head
            head = head.next
        return nodes_dict.get(cnt // 2 + 1)