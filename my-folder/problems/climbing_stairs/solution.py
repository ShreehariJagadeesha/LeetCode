class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return n
        prev1=1
        prev2=2
        curr=0
        for i in range(2,n):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr
        return curr