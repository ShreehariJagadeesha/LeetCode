class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        counter = 0
        for i in range(1,n+1):
              while i%5==0:
                    counter =counter + 1
                    i =i/5
        return int(counter)