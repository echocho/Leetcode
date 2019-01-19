class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.dict[key] = 'Y'

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        try:
            self.dict.pop(key)
        except:
            pass
        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.dict.get(key) == 'Y'
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)