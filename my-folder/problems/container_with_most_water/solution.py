class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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