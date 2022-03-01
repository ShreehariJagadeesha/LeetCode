class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        N,M=len(obstacleGrid[0]),len(obstacleGrid)
        dp=[[0 for col in range(N)] for row in range(M)]
        for c in range(N):
            if obstacleGrid[0][c]==1:break
            else:
                dp[0][c]=1
        for r in range(M):
            if obstacleGrid[r][0]==1:break
            else:
                dp[r][0]=1
                
        for c in range(1,N):
            for r in range(1,M):
                if obstacleGrid[r][c]==1:continue
                dp[r][c]=dp[r][c-1]+dp[r-1][c]
                    
        print dp
        return dp[-1][-1]
            
            