class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        if target<nums[0]:
            return 0
        if target>nums[length-1]:
            return length
        if length==1 and target==nums[0]:
            return 0            
        for i in range(0,len(nums)):
            if target==nums[i]:
                return i
            else:
                if target > nums[i] and target < nums[i+1]:
                    return i+1