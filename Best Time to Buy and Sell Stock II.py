class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i = 0
        # get the everyday difference
        while i < len(prices)-1:
            dif = prices[i+1] - prices[i]
            if dif > 0:
                profit += dif
            i += 1
        return profit
