class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        setB = set(B)
        sumA, sumB = sum(A), sum(B)
        for x in A:
            if x + (sumB - sumA) / 2 in setB:
                return [x, int(x + (sumB - sumA) / 2)]