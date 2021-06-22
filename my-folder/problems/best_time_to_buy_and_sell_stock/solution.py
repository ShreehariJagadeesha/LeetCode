class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currmax=0
        globalmax=0 
        
        for i in range(1,len(prices)):
            currmax=max(currmax+(prices[i]-prices[i-1]),0)
            globalmax=max(currmax,globalmax)
            
        return globalmax