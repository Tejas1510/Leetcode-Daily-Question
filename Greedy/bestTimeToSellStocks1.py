# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min1=100001
        max1=0
        for i in range(len(prices)):
            if(prices[i]<min1):
                min1=prices[i]
            elif(prices[i]-min1>max1):
                max1=prices[i]-min1
        return max1
            