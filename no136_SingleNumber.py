class Solution1(object):
	# use built-in collections.Counter to count occurances
	# O(n)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k

class Solution2(object):
	# use hash table: pop 