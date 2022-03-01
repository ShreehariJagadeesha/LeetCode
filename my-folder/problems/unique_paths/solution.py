class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0 for col in range(m)] for row in range(n)]
        for i in range(m):dp[0][i]=1
        for j in range(n):dp[j][0]=1
            
        for row in range(1,n):
            for col in range(1,m):
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
                
        return dp[n-1][m-1]