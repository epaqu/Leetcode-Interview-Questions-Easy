# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary(n, m):
            """
            checks the midpoint of n and m for isBadVersion
            """
            if isBadVersion((n+m)//2):
                if not isBadVersion((n+m)//2 - 1):
                    return (n+m)//2
                return binary((n+m)//2, m)
            else:
                if isBadVersion((n+m)//2 + 1):
                    return (n+m)//2+1
                return binary(n, (n+m)//2)
        return binary(n, 1)
