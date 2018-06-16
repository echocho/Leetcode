# Leetcode155_minStack.py
'''
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2. '''

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = [0]
        self.currentSize = 0
        self.stack = []

    def percUp(self, i):
        while i//2 > 0:
            if self.heap[i] <= self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.heap.append(x)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def minChild(self, i):
        if i * 2 >= self.currentSize:
            return i * 2
        if i * 2 +1 <= self.currentSize:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return i * 2 + 1
            return i * 2

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heap[mc] < self.heap[i]:
                self.heap[mc], self.heap[i] = self.heap[i], self.heap[mc]
            i = mc

    def pop(self):
        """
        :rtype: void
        """
        rm = self.stack[-1]
        del(self.stack[-1])
        if rm == self.heap[1]:
            self.heap[1] = self.heap[self.currentSize]
            self.percDown(1)
            del(self.heap[-1])
            self.currentSize -= 1
        else:
            self.heap.remove(rm)
            self.currentSize -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.heap[1]

ms = MinStack()
ms.push(2)
ms.push(0)
ms.push(3)
ms.push(0)
print(ms.stack)
print(ms.heap)
print('min',ms.getMin())
ms.pop()
print('pop')
print(ms.stack)
print(ms.heap)
print('min',ms.getMin())
ms.pop()
print('pop')
print(ms.stack)
print(ms.heap)
print('min',ms.getMin())
ms.pop()
print('pop')
print(ms.stack)
print(ms.heap)
print('min',ms.getMin())
# print('min',ms.getMin())
# ms.pop()
# print('pop', ms.stack, ms.heap)
# print('min',ms.getMin())
# ms.pop()
# print('pop', ms.stack, ms.heap)
# print('min',ms.getMin())
# print(ms.stack)
# print(ms.heap)
# ms.push(2)
# ms.push(7)
# ms.push(4)
# ms.push(9)
# ms.push(3)
# ms.push(10)
# ms.push(6)
# ms.push(1)
# ms.push(8)
# ms.push(11)
# # ms.push(12)
# print(ms.stack)
# print(ms.heap)
# # print(ms.top())
# # print(ms.getMin())
# ms.pop()
# print('pop 1 out')
# print(ms.stack)
# print(ms.heap)
# ms.pop()
# print('pop 1 out')
# print(ms.stack)
# print(ms.heap)

'''remove() 和del() 的区别：'''
