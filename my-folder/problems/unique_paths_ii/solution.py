class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
                
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            if obstacleGrid[r][0]==1:break
            dp[r][0]=1
        
        for c in range(n):
            if obstacleGrid[0][c]==1:break
            dp[0][c]=1
                
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c]==1:
                    dp[r][c]=0
                else:
                    dp[r][c]=dp[r-1][c]+dp[r][c-1]
        
        return dp[-1][-1]