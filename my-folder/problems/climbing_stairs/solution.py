class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n
        
        list=[0 for i in range(n+1)]
        
        for i in range(len(list)):
            if(i<4):
                list[i]=i
            else:
                list[i]=list[i-1]+list[i-2]
            
        return list[-1]
