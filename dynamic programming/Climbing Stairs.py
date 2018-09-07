class Solution(object):
    def factorial(self, n):
        if n == 0 or n==1:
            return 1
        return n*self.factorial(n-1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        for k 2s, (n-k)!/((n-2k)!k!) ways
        there are many possible values for k
        #k = n//2
        """
        res = 0
        for k in range(0,n//2+1):
            res += self.factorial(n-k) / (self.factorial(n-2*k) * self.factorial(k))
        return res
