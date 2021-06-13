class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        zeroslist=[]
        while (count<len(nums)):
            if nums[count]==0:
                zeroslist.append(nums.pop(count))
            else:
                count=count+1
        
        nums.extend(zeroslist)
        return nums