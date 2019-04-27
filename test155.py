import unittest

from Leetcode155_minStack import MinStack2

class TestMinStack2(unittest.TestCase):

    def test_all(self):
        """not duplicate element pushed"""
        self.stack = MinStack2()
        lst1 = [-2, 7, 0, -6, 9]
        for i in lst1:
            self.stack.push(i)
        self.assertEqual(self.stack.top(), 9)
        self.assertEqual(self.stack.getMin(), -6)
        self.assertEqual(self.stack.pop(), None)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), -2)
        self.assertEqual(self.stack.top(), 0)

    def test_all2(self):
        """push duplicate elements"""
        self.stack = MinStack2()
        self.stack.push(2)
        self.stack.push(-3)
        self.stack.push(-3)
        self.assertEqual(self.stack.getMin(), -3)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), -3)

if __name__ == '__main__':
    unittest.main()
