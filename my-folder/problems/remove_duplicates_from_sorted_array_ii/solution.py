class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return len(nums)
        i=0
        while(i<len(nums)-2):
            if nums[i]==nums[i+1] and  nums[i]==nums[i+2]:
                nums.pop(i+2)
            else:
                i=i+1
        return len(nums)