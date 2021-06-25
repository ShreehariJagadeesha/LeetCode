class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         # if there is only 1 house, return that house
#         if len(nums) == 1:
#             return nums[0]

#         # dp[i] is the max profit choosing up to and including the i-th house (0 indexed)
#         dp = [0] * len(nums)
        
#         # base cases
#         # if only including the first house, choose that house
#         # if including the first two houses, choose whichever house is higher
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
#         # fill in the rest one extra house at a time
#         for i in range(2, len(nums)):
#             # we can either:
#             # 1. rob this house but do not rob the previous house
#             # 2. skip this house
#             # choose the most profitable option
#             dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

#         return dp[len(nums) - 1]
        
        if not nums:
            return 0
        if len(nums)<3:return max(nums)
        
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
            
        return dp[-1]
            
        