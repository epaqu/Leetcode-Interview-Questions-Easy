class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        while x != 0:
            result *= 10
            result += x%10
            x = int(x/10)
        if sign*result > 2**31-1 or sign*result < -2**31:
            return 0
        else:
            return sign*result
