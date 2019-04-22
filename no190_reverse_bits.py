# O(N)
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_str = bin(n)[2:]
        target_bin_str = bin_str[::-1]
        if len(bin_str) < 32:
            target_bin_str += '0' * (32 - len(bin_str))
        return int(target_bin_str, 2)