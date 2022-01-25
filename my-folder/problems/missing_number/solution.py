class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rangesum=0
        sumnum=sum(nums)
        for i in range(len(nums)+1):
            rangesum=rangesum+i
        if rangesum!=sumnum:
            return rangesum-sumnum
        return 0        