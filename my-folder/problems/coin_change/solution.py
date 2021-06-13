class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[float('inf') for x in range(amount+1)]
        dp[0]=0
        
        for i in range(len(dp)):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
                    
        return -1 if dp[-1]==float('inf') else dp[-1]
        