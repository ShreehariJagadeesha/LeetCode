class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.rob1(nums[1:]),self.rob1(nums[:-1]))
    
    def rob1(self,nums):
        arr = [0] * (len(nums) + 1)
        arr[1] = nums[0]
        arr[2] = max(nums[0],nums[1])
        for i in range(3,len(arr)):
            arr[i] = max(nums[i - 1] + arr[i - 2],arr[i - 1])
        return arr[-1]