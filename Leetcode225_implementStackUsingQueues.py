# Leetcode225_implementStackUsingQueues.py
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.

class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queueList = []
        self.currentSize = 0
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queueList.append(x)
        self.currentSize += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.currentSize >= 1:
            self.queueList = self.queueList[::-1]
            remval = self.queueList[0]
            self.queueList.remove(self.queueList[0])
            self.currentSize -= 1
            self.queueList = self.queueList[::-1]
            return remval

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queueList[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.currentSize == 0

s = MyStack()
# s.push(None)
s.push(1)
s.push(2)
# s.push(None)        
print(s.queueList)
# s.pop()
# print(s.queueList)
# s.pop()
# print(s.queueList)
# print(s.empty())
print(s.top())
