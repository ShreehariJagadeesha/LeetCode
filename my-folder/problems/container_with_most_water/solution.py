class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # temp=[]
        # for i in range(0,len(height)):
        #     for j in range(0,len(height)):
        #         if i!=j:
        #             if height[i]>height[j]:
        #                 temp.append(height[j]*abs(i-j))
        #             else:
        #                 temp.append(height[i]*abs(i-j))
        # return max(temp)
    
        i = 0
        j = len(height) - 1
        res = 0
        curr=0
        while i < j:
            if height[i]>height[j]:
                curr = (j - i) * height[j]
            else:
                curr = (j - i) * height[i]
            if curr > res:
                res = curr
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
                
        

            
        