# generate indeices using random lib

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.shuffled = [0] * len(self.original)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        new_indices = random.sample(range(len(self.original)), len(self.original))
        for (idx, num) in list(zip(new_indices, self.original)):
            self.shuffled[idx] = num
        return self.shuffled



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()