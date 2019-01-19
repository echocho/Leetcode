class Solution1:
    # recursion
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)

class Solution2:
    # dynamic programming
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        res = [0] * N
        res[0], res[1] = 1, 1
        for i in range(2, N):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]
