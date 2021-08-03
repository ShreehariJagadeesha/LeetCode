class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return -1,-1
        if len(nums) == 1 and target in nums:
            return 0,0
        if target in nums:
            x = nums.count(target)
            y = nums.index(target)
            return y,x+y-1
        else:
            return -1,-1