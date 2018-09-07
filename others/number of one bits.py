class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = []
        while n>0:
            binary.append(n%2)
            n = n//2
        return sum(binary)
