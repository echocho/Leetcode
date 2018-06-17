# Leetcode206_reverseLinkedList.py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1: recursive
        # O(n)
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

        # Solution 2: iterative
        # O(n)
        '''
        node_prev = None
        node_curr = head
        while node_curr:
            node_temp = node_curr.next
            node_curr.next = node_prev
            node_prev = node_curr
            node_curr = node_temp
            # Note: we need node_temp to store the next node, otherwise, after altering the node_curr's next pointer, 
            # we can go on to the one which yet to be iterate.
            # In otherwords, the following line is not replaceable with the above four lines
            node_curr.next, node_prev, node_curr = node_prev, node_curr, node_curr.next
        return node_prev
        '''


# implement a linked list with reverse method, just for fun
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.val = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        cnt = 0
        while current != None:
            cnt += 1
            current = current.getNext()
        return cnt

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def reverse(self):
        current = self.head
        previous = None
        while current:
            previous = current
            current = current.getNext()
            previous.getNext().setNext(previous)
        return self.head

# lst = UnorderedList()
# lst.add(1)
# lst.add(2)
# lst.add(3)
# lst.add(4)
# lst.add(5)
# lst.add(6)
# print(lst.reverse())
















