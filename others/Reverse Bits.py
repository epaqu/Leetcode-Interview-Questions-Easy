import numpy as np

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = []
        res = 0
        for i in range(0, 32):
            binary.insert(0, n%2)
            n = n//2
        for i in range(0, len(binary)):
            res += binary[i] * np.power(2,i)
        return res
