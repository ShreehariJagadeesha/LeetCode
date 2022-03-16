class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mx=0
        l=0
        n=len(height)
        r=n-1
        
        while l<r:
            width=r-l
            h=min(height[l],height[r])
            mx=max(mx,width*h)
            
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return mx