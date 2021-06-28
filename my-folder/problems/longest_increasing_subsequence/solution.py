class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         if not nums:
#             return 0
#         n=len(nums)
#         dp=[1]*n
        
#         count=[1]*n
        
#         for i in range(n):
#             for j in range(i):
#                 if nums[i]>nums[j]:
#                     if dp[j]+1>dp[i]:
#                         dp[i]=dp[j]+1
#                         count[i]=count[j]
#                     elif dp[j]+1==dp[i]:
#                         count[i]+=count[j]
#         longes_len=max(dp)
        
#         return sum([count[i] for i in range(n) if dp[i]==longes_len])
        dp = [1]*(len(nums))
        for i, c in enumerate(nums):
            tmp = [dp[j]+1 for j in range(i) if c > nums[j]]
            if tmp:
                dp[i] = max(tmp)
        return max(dp)