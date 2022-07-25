class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1
        
        while l<r:
            cursum=numbers[l]+numbers[r]
            
            if cursum<target:
                l=l+1
            elif cursum>target:
                r=r-1
            else:
                return [l+1,r+1]
        return[]