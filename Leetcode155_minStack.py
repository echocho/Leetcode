# Leetcode155_minStack.py

# Solution: use binary heap as the backbone, to have faster run time
# Time complexity:
# getMin(): O(1)
# top(): O(1)
# push(): O(log n)
# pop(): O(log n)

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

class MinStack2:
    """
    use two lists: one stores all elements and another stores smallest items seen so far
    Time complexity:
    getMin(): O(1)
    pop(): O(1)
    push(): O(1)
    top(): O(1)
    """
    def __init__(self):
        self.min_elems = []
        self.elems = []

    def push(self, x):
        if not self.elems:
            self.min_elems.append(x)
        elif x <= self.min_elems[-1]:
            self.min_elems.append(x)
        self.elems.append(x)

    def pop(self):
        if self.__stack_is_empty():
            raise Exception('Empty stack')
        t = self.elems.pop()
        if t == self.min_elems[-1]:
            self.min_elems.pop()

    def top(self):
        if self.__stack_is_empty():
            raise Exception('Empty stack')
        return self.elems[-1]

    def getMin(self):
        if self.__stack_is_empty():
            raise Exception('Empty stack')
        return self.min_elems[-1]

    def __stack_is_empty(self):
        return len(self.elems) == 0
