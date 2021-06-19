class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # temp=deque(nums)
        # print(temp)
        # for i in range(0,k):
        #     temp.appendleft(temp.pop())
        # print(temp)
        # nums=list(temp)
        # print(nums)
        
        k%=len(nums)
        
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]