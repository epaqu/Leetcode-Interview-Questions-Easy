class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        highest = 0
        buy_price = prices[0]
        for i in range(0, len(prices)):
            if prices[i] > buy_price:
                highest = max(highest, prices[i] - buy_price)
            else:
                buy_price = prices[i]
        #you can do this because you save the highest profit in highest.
        return highest
