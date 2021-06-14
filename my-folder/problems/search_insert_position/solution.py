class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            else:
                nums.append(target)
                
        nums.sort()
        
        for i in range(len(nums)):
            if target==nums[i]:
                return i
                
        
            
        