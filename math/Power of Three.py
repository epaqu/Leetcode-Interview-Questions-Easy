class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 3:
            return True
        if n % 3 != 0 or n == 0:
            return False
        return self.isPowerOfThree(n/3)
